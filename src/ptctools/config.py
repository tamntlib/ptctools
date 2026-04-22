"""Docker Swarm Config management commands via Portainer API."""

from __future__ import annotations

import json
import logging
import os
import sys
import time
import traceback
from pathlib import Path

import click
import docker.errors

from ptctools._portainer import (
    get_portainer_api_client,
    get_portainer_docker_client,
    PortainerError,
    ResourceControlError,
)
from ptctools.portainer_client.openapi_client.api.users_api import UsersApi
from ptctools.portainer_client.openapi_client.api.resource_controls_api import (
    ResourceControlsApi,
)
from ptctools.portainer_client.openapi_client.models.resourcecontrols_resource_control_create_payload import (
    ResourcecontrolsResourceControlCreatePayload,
)
from ptctools.portainer_client.openapi_client.models.resourcecontrols_resource_control_update_payload import (
    ResourcecontrolsResourceControlUpdatePayload,
)
from ptctools.portainer_client.openapi_client.models.portainer_resource_control_type import (
    PortainerResourceControlType,
)
from ptctools.portainer_client.openapi_client.exceptions import ApiException

logger = logging.getLogger(__name__)


class ConfigError(PortainerError):
    """Exception for Docker config operations."""

    pass


def _find_services_using_config(client, config_id: str, config_name: str) -> list[dict]:
    """Find all services referencing a specific config."""
    results = []
    for service in client.services.list():
        spec = service.attrs.get("Spec", {})
        task_template = spec.get("TaskTemplate", {})
        container_spec = task_template.get("ContainerSpec", {})
        configs = container_spec.get("Configs") or []

        matching_refs = [
            cfg_ref for cfg_ref in configs
            if cfg_ref.get("ConfigID") == config_id or cfg_ref.get("ConfigName") == config_name
        ]

        if matching_refs:
            mode = spec.get("Mode", {})
            replicated = mode.get("Replicated")
            replicas = replicated.get("Replicas") if replicated else None

            results.append({
                "service": service,
                "replicas": replicas,
                "config_refs": matching_refs,
            })

    return results


def _update_service_spec(client, service, spec: dict) -> None:
    """Update a service using its full spec dict via the low-level API."""
    service.reload()
    version = service.attrs["Version"]["Index"]
    client.api.update_service(
        service.id,
        version,
        task_template=spec.get("TaskTemplate"),
        name=spec.get("Name"),
        mode=spec.get("Mode"),
        labels=spec.get("Labels"),
        update_config=spec.get("UpdateConfig"),
        endpoint_spec=spec.get("EndpointSpec"),
        rollback_config=spec.get("RollbackConfig"),
        fetch_current_spec=True,
    )


def _wait_for_service_scale(service, target_replicas: int, timeout: int = 120) -> bool:
    """Wait for a service to reach the target number of running tasks."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        service.reload()
        tasks = service.tasks(filters={"desired-state": "running"})
        running = sum(1 for t in tasks if t.get("Status", {}).get("State") == "running")
        if target_replicas == 0 and running == 0:
            return True
        if target_replicas > 0 and running >= target_replicas:
            return True
        time.sleep(2)
    return False


def _print_recovery_info(affected: list[dict], config_name: str) -> None:
    """Print recovery information when the replacement process fails midway."""
    click.echo("", err=True)
    click.echo("=== RECOVERY INFO ===", err=True)
    click.echo(f"Config being replaced: {config_name}", err=True)
    click.echo("Affected services and their original replica counts:", err=True)
    for info in affected:
        svc_name = info["service"].attrs.get("Spec", {}).get("Name", "?")
        replicas = info["replicas"]
        r_str = f"{replicas}" if replicas is not None else "global"
        click.echo(f"  - {svc_name} (original replicas: {r_str})", err=True)
    click.echo("", err=True)
    click.echo("To recover manually:", err=True)
    click.echo("  1. Check service states: docker service ls", err=True)
    click.echo("  2. Restore replicas: docker service scale <name>=<replicas>", err=True)
    click.echo("  3. Re-add config refs if needed: docker service update --config-add ...", err=True)
    click.echo("=====================", err=True)


@click.group()
def cli():
    """Docker Swarm Config management commands."""
    pass


@cli.command("set")
@click.option(
    "--url",
    "-u",
    envvar="PORTAINER_URL",
    required=True,
    help="Portainer base URL (or PORTAINER_URL env var)",
)
@click.option("--name", "-n", required=True, help="Config name")
@click.option("--data", "-d", default=None, help="Config data (string content)")
@click.option(
    "--file",
    "-f",
    "file_path",
    type=click.Path(exists=True, path_type=Path),
    default=None,
    help="Read config data from file",
)
@click.option("--endpoint-id", "-e", type=int, default=1, help="Portainer endpoint ID")
@click.option("--force", is_flag=True, help="Replace existing config if it exists")
@click.option(
    "--ownership",
    type=click.Choice(["private", "team", "public"]),
    help="Access control",
)
@click.option("--team-id", "-t", type=int, help="Team ID for team ownership")
def set_config(
    url: str,
    name: str,
    data: str | None,
    file_path: Path | None,
    endpoint_id: int,
    force: bool,
    ownership: str | None,
    team_id: int | None,
):
    """Create or update a Docker Swarm config.

    Examples:

        # Create from inline data
        ptctools docker config set -u https://portainer.example.com -n my-config -d "config content"

        # Create from file
        ptctools docker config set -u https://portainer.example.com -n nginx.conf -f ./nginx.conf

        # Replace existing config
        ptctools docker config set -u https://portainer.example.com -n my-config -d "new content" --force
    """
    # Validate that exactly one of --data or --file is provided
    if data is None and file_path is None:
        click.echo("Error: Either --data or --file must be provided", err=True)
        sys.exit(1)
    if data is not None and file_path is not None:
        click.echo("Error: Cannot use both --data and --file", err=True)
        sys.exit(1)

    # Read data from file if provided
    if file_path is not None:
        data = file_path.read_text()

    access_token = os.environ.get("PORTAINER_ACCESS_TOKEN")
    if not access_token:
        click.echo(
            "Error: Missing PORTAINER_ACCESS_TOKEN environment variable", err=True
        )
        sys.exit(1)

    portainer_url = url.rstrip("/")

    # Auto-detect team if needed
    if ownership == "team" and not team_id:
        try:
            with get_portainer_api_client(portainer_url, access_token) as api_client:
                users_api = UsersApi(api_client)
                user = users_api.current_user_inspect()
                memberships = users_api.user_memberships_inspect(user.id)
                user_teams = []
                for m in memberships:
                    if m.team_id:
                        user_teams.append(
                            {"Id": m.team_id, "Name": f"Team {m.team_id}"}
                        )

                if user_teams:
                    team_id = user_teams[0]["Id"]
                    click.echo(
                        f"Auto-detected team: {user_teams[0]['Name']} (ID: {team_id})"
                    )
                else:
                    click.echo(
                        "Error: ownership=team but no team found and --team-id not specified",
                        err=True,
                    )
                    sys.exit(1)
        except ApiException as e:
            logger.error("Failed to get user teams: %s\n%s", e, traceback.format_exc())
            click.echo(f"Error: Failed to get user teams: {e}", err=True)
            sys.exit(1)

    try:
        client = get_portainer_docker_client(portainer_url, access_token, endpoint_id)

        # Check if config already exists
        existing = None
        for config in client.configs.list():
            if config.name == name:
                existing = config
                break

        need_reattach = None

        if existing:
            if not force:
                click.echo(
                    f"Error: Config '{name}' already exists. Use --force to replace.",
                    err=True,
                )
                sys.exit(1)

            # Try simple removal first
            click.echo(f"Removing existing config: {name}")
            try:
                existing.remove()
            except docker.errors.APIError as remove_err:
                err_str = str(remove_err).lower()
                if "in use" not in err_str:
                    raise

                click.echo(f"Config '{name}' is in use by services. Performing safe replacement...")

                # Phase 1: Discover affected services
                affected = _find_services_using_config(client, existing.id, name)
                if not affected:
                    click.echo("Error: Config is reported as in use but no referencing services found.", err=True)
                    click.echo(f"Original error: {remove_err}", err=True)
                    sys.exit(1)

                service_names = [
                    s["service"].attrs.get("Spec", {}).get("Name", s["service"].id[:12])
                    for s in affected
                ]
                click.echo(f"  Found {len(affected)} service(s) using this config: {', '.join(service_names)}")

                # Phase 2: Scale replicated services to 0
                click.echo("  Scaling services to 0 replicas...")
                for info in affected:
                    svc = info["service"]
                    svc_name = svc.attrs.get("Spec", {}).get("Name", svc.id[:12])
                    replicas = info["replicas"]

                    if replicas is None:
                        click.echo(f"    {svc_name}: global mode (will update in-place)")
                        continue

                    click.echo(f"    {svc_name}: {replicas} -> 0 replicas")
                    try:
                        svc.reload()
                        spec = svc.attrs["Spec"]
                        spec["Mode"]["Replicated"]["Replicas"] = 0
                        _update_service_spec(client, svc, spec)
                    except docker.errors.APIError as e:
                        click.echo(f"Error: Failed to scale {svc_name} to 0: {e}", err=True)
                        _print_recovery_info(affected, name)
                        sys.exit(1)

                # Wait for services to drain
                for info in affected:
                    svc = info["service"]
                    svc_name = svc.attrs.get("Spec", {}).get("Name", svc.id[:12])
                    if info["replicas"] is None:
                        continue
                    click.echo(f"    Waiting for {svc_name} to drain...")
                    if not _wait_for_service_scale(svc, 0):
                        click.echo(f"    Warning: {svc_name} did not fully drain within timeout. Proceeding anyway.")

                # Phase 3: Remove config references from all services
                click.echo("  Removing config references from services...")
                for info in affected:
                    svc = info["service"]
                    svc_name = svc.attrs.get("Spec", {}).get("Name", svc.id[:12])
                    svc.reload()

                    spec = svc.attrs["Spec"]
                    container_spec = spec["TaskTemplate"]["ContainerSpec"]
                    current_configs = container_spec.get("Configs") or []

                    updated_configs = [
                        c for c in current_configs
                        if c.get("ConfigID") != existing.id and c.get("ConfigName") != name
                    ]
                    container_spec["Configs"] = updated_configs

                    click.echo(f"    Updating {svc_name} (removing config ref)...")
                    try:
                        _update_service_spec(client, svc, spec)
                    except docker.errors.APIError as e:
                        click.echo(f"Error: Failed to update {svc_name}: {e}", err=True)
                        _print_recovery_info(affected, name)
                        sys.exit(1)

                # Phase 4: Delete the old config
                click.echo(f"  Deleting old config '{name}'...")
                try:
                    existing.reload()
                    existing.remove()
                except docker.errors.APIError as e:
                    click.echo(f"Error: Still cannot remove config: {e}", err=True)
                    _print_recovery_info(affected, name)
                    sys.exit(1)

                need_reattach = affected

        click.echo(f"Creating config: {name}")
        new_config = client.configs.create(name=name, data=data.encode("utf-8"))
        click.echo(f"✓ Config '{name}' created successfully (ID: {new_config.id})")

        # Reattach config to services and restore replicas
        if need_reattach:
            new_config_id = new_config.id
            click.echo("  Re-adding config references to services...")

            for info in need_reattach:
                svc = info["service"]
                svc_name = svc.attrs.get("Spec", {}).get("Name", svc.id[:12])
                svc.reload()

                spec = svc.attrs["Spec"]
                container_spec = spec["TaskTemplate"]["ContainerSpec"]
                current_configs = container_spec.get("Configs") or []

                for orig_ref in info["config_refs"]:
                    new_ref = {
                        "ConfigID": new_config_id,
                        "ConfigName": name,
                        "File": orig_ref.get("File", {}),
                    }
                    current_configs.append(new_ref)

                container_spec["Configs"] = current_configs

                click.echo(f"    Updating {svc_name} (re-adding config ref)...")
                try:
                    _update_service_spec(client, svc, spec)
                except docker.errors.APIError as e:
                    click.echo(f"Error: Failed to re-add config to {svc_name}: {e}", err=True)
                    click.echo(f"New config '{name}' (ID: {new_config_id}) was created but not attached to {svc_name}.", err=True)
                    click.echo("You may need to manually update this service.", err=True)

            # Restore original replica counts
            click.echo("  Restoring service replica counts...")
            for info in need_reattach:
                svc = info["service"]
                svc_name = svc.attrs.get("Spec", {}).get("Name", svc.id[:12])
                replicas = info["replicas"]

                if replicas is None:
                    continue

                click.echo(f"    {svc_name}: 0 -> {replicas} replicas")
                svc.reload()
                spec = svc.attrs["Spec"]
                spec["Mode"]["Replicated"]["Replicas"] = replicas

                try:
                    _update_service_spec(client, svc, spec)
                except docker.errors.APIError as e:
                    click.echo(f"Error: Failed to restore {svc_name} to {replicas} replicas: {e}", err=True)
                    click.echo("You may need to manually scale this service.", err=True)

            click.echo("  Config replacement complete.")

        # Apply access control
        if ownership:
            click.echo()
            config_id = new_config.id
            rc_id = new_config.attrs.get("Portainer", {}).get("ResourceControl", {}).get("Id")

            with get_portainer_api_client(portainer_url, access_token) as api_client:
                rc_api = ResourceControlsApi(api_client)

                if ownership == "private":
                    users_api = UsersApi(api_client)
                    user = users_api.current_user_inspect()
                    click.echo("Setting access control to private...")
                    if rc_id:
                        rc_payload = ResourcecontrolsResourceControlUpdatePayload(
                            public=False,
                            teams=[],
                            users=[user.id],
                        )
                        rc_api.resource_control_update(id=rc_id, body=rc_payload.to_dict())
                    else:
                        rc_payload = ResourcecontrolsResourceControlCreatePayload(
                            resource_id=config_id,
                            type=PortainerResourceControlType.ConfigResourceControl,
                            public=False,
                            teams=[],
                            users=[user.id],
                        )
                        rc_api.resource_control_create(body=rc_payload.to_dict())
                    click.echo("✓ Access control set to private")

                elif ownership == "team" and team_id:
                    click.echo(f"Setting access control for team {team_id}...")
                    if rc_id:
                        rc_payload = ResourcecontrolsResourceControlUpdatePayload(
                            public=False,
                            teams=[team_id],
                            users=[],
                        )
                        rc_api.resource_control_update(id=rc_id, body=rc_payload.to_dict())
                    else:
                        rc_payload = ResourcecontrolsResourceControlCreatePayload(
                            resource_id=config_id,
                            type=PortainerResourceControlType.ConfigResourceControl,
                            public=False,
                            teams=[team_id],
                            users=[],
                        )
                        rc_api.resource_control_create(body=rc_payload.to_dict())
                    click.echo(f"✓ Access control set to team {team_id}")

                elif ownership == "public":
                    click.echo("Setting access control to public...")
                    if rc_id:
                        rc_payload = ResourcecontrolsResourceControlUpdatePayload(
                            public=True,
                            teams=[],
                            users=[],
                        )
                        rc_api.resource_control_update(id=rc_id, body=rc_payload.to_dict())
                    else:
                        rc_payload = ResourcecontrolsResourceControlCreatePayload(
                            resource_id=config_id,
                            type=PortainerResourceControlType.ConfigResourceControl,
                            public=True,
                            teams=[],
                            users=[],
                        )
                        rc_api.resource_control_create(body=rc_payload.to_dict())
                    click.echo("✓ Access control set to public")

    except docker.errors.APIError as e:
        logger.error("Config operation failed: %s\n%s", e, traceback.format_exc())
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except ApiException as e:
        error_msg = str(e.body) if e.body else str(e.reason)
        logger.error("Config operation failed: %s\n%s", error_msg, traceback.format_exc())
        click.echo(f"Error: {error_msg}", err=True)
        sys.exit(1)


@cli.command("get")
@click.option(
    "--url",
    "-u",
    envvar="PORTAINER_URL",
    required=True,
    help="Portainer base URL (or PORTAINER_URL env var)",
)
@click.option("--name", "-n", required=True, help="Config name")
@click.option("--endpoint-id", "-e", type=int, default=1, help="Portainer endpoint ID")
def get_config_cmd(url: str, name: str, endpoint_id: int):
    """Get details of a Docker Swarm config by name.

    Note: Docker API does not return the actual config data for security reasons.
    """
    access_token = os.environ.get("PORTAINER_ACCESS_TOKEN")
    if not access_token:
        click.echo(
            "Error: Missing PORTAINER_ACCESS_TOKEN environment variable", err=True
        )
        sys.exit(1)

    portainer_url = url.rstrip("/")

    try:
        client = get_portainer_docker_client(portainer_url, access_token, endpoint_id)

        config = None
        for c in client.configs.list():
            if c.name == name:
                config = c
                break

        if config:
            click.echo(json.dumps(config.attrs, indent=2))
        else:
            click.echo(f"Error: Config '{name}' not found", err=True)
            sys.exit(1)

    except docker.errors.APIError as e:
        logger.error("Config operation failed: %s\n%s", e, traceback.format_exc())
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@cli.command("list")
@click.option(
    "--url",
    "-u",
    envvar="PORTAINER_URL",
    required=True,
    help="Portainer base URL (or PORTAINER_URL env var)",
)
@click.option("--endpoint-id", "-e", type=int, default=1, help="Portainer endpoint ID")
def list_configs_cmd(url: str, endpoint_id: int):
    """List all Docker Swarm configs."""
    access_token = os.environ.get("PORTAINER_ACCESS_TOKEN")
    if not access_token:
        click.echo(
            "Error: Missing PORTAINER_ACCESS_TOKEN environment variable", err=True
        )
        sys.exit(1)

    portainer_url = url.rstrip("/")

    try:
        client = get_portainer_docker_client(portainer_url, access_token, endpoint_id)
        configs = client.configs.list()
    except docker.errors.APIError as e:
        logger.error("Config operation failed: %s\n%s", e, traceback.format_exc())
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)

    if not configs:
        click.echo("No configs found.")
        return

    click.echo(f"Found {len(configs)} config(s):\n")
    for config in configs:
        config_id = config.id
        config_name = config.name
        created = config.attrs.get("CreatedAt", "unknown")
        click.echo(f"  {config_name}")
        click.echo(f"    ID: {config_id}")
        click.echo(f"    Created: {created}")
        click.echo()


@cli.command("delete")
@click.option(
    "--url",
    "-u",
    envvar="PORTAINER_URL",
    required=True,
    help="Portainer base URL (or PORTAINER_URL env var)",
)
@click.option("--name", "-n", required=True, help="Config name")
@click.option("--endpoint-id", "-e", type=int, default=1, help="Portainer endpoint ID")
def delete_config_cmd(url: str, name: str, endpoint_id: int):
    """Delete a Docker Swarm config by name."""
    access_token = os.environ.get("PORTAINER_ACCESS_TOKEN")
    if not access_token:
        click.echo(
            "Error: Missing PORTAINER_ACCESS_TOKEN environment variable", err=True
        )
        sys.exit(1)

    portainer_url = url.rstrip("/")

    try:
        client = get_portainer_docker_client(portainer_url, access_token, endpoint_id)

        config = None
        for c in client.configs.list():
            if c.name == name:
                config = c
                break

        if not config:
            click.echo(f"Error: Config '{name}' not found", err=True)
            sys.exit(1)

        click.echo(f"Deleting config: {name} (ID: {config.id})")
        config.remove()
        click.echo(f"✓ Config '{name}' deleted successfully")

    except docker.errors.APIError as e:
        logger.error("Config operation failed: %s\n%s", e, traceback.format_exc())
        click.echo(f"Error: Failed to delete config: {e}", err=True)
        sys.exit(1)
