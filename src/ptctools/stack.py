"""Stack management commands."""

from __future__ import annotations

import json
import logging
import os
import sys
import traceback
from pathlib import Path

import click

from ptctools._portainer import (
    get_portainer_api_client,
    get_portainer_docker_client,
    PortainerError,
    ResourceControlError,
)
from ptctools.portainer_client.openapi_client.api.stacks_api import StacksApi
from ptctools.portainer_client.openapi_client.api.users_api import UsersApi
from ptctools.portainer_client.openapi_client.api.resource_controls_api import ResourceControlsApi
from ptctools.portainer_client.openapi_client.models.stacks_swarm_stack_from_file_content_payload import StacksSwarmStackFromFileContentPayload
from ptctools.portainer_client.openapi_client.models.stacks_update_swarm_stack_payload import StacksUpdateSwarmStackPayload
from ptctools.portainer_client.openapi_client.models.resourcecontrols_resource_control_create_payload import ResourcecontrolsResourceControlCreatePayload
from ptctools.portainer_client.openapi_client.models.resourcecontrols_resource_control_update_payload import ResourcecontrolsResourceControlUpdatePayload
from ptctools.portainer_client.openapi_client.models.portainer_resource_control_type import PortainerResourceControlType
from ptctools.portainer_client.openapi_client.exceptions import ApiException

logger = logging.getLogger(__name__)


class StackError(PortainerError):
    """Exception for stack operations."""
    pass


def load_stack_env_file(env_path: Path) -> list[dict]:
    """Parse .env file into Portainer environment variable format."""
    env_vars = []

    if not env_path.exists():
        return env_vars

    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                name, value = line.split("=", 1)
                name = name.strip()
                if name:
                    env_vars.append({"name": name, "value": value})

    return env_vars


@click.group()
def cli():
    """Stack management commands."""
    pass


@cli.command()
@click.option("--url", "-u", required=True, help="Portainer base URL")
@click.option("--stack-name", "-n", required=True, help="Stack name")
@click.option(
    "--stack-file",
    "-f",
    required=True,
    type=click.Path(exists=True, path_type=Path),
    help="Path to compose file",
)
@click.option("--endpoint-id", "-e", type=int, default=1, help="Portainer endpoint ID")
@click.option(
    "--env-file", type=click.Path(path_type=Path), help="Path to stack .env file"
)
@click.option(
    "--ownership",
    type=click.Choice(["private", "team", "public"]),
    help="Access control",
)
@click.option("--team-id", "-t", type=int, help="Team ID for team ownership")
def deploy(
    url: str,
    stack_name: str,
    stack_file: Path,
    endpoint_id: int,
    env_file: Path | None,
    ownership: str | None,
    team_id: int | None,
):
    """Deploy or update a stack in Portainer."""
    access_token = os.environ.get("PORTAINER_ACCESS_TOKEN")
    if not access_token:
        click.echo(
            "Error: Missing PORTAINER_ACCESS_TOKEN environment variable", err=True
        )
        sys.exit(1)

    portainer_url = url.rstrip("/")
    stack_file = stack_file.resolve()
    env_file = env_file.resolve() if env_file else stack_file.parent / ".env"

    # Auto-detect team if needed
    if ownership == "team" and not team_id:
        try:
            with get_portainer_api_client(portainer_url, access_token) as client:
                users_api = UsersApi(client)
                user = users_api.current_user_inspect()
                memberships = users_api.user_memberships_inspect(user.id)
                user_teams = []
                for m in memberships:
                    if m.team_id:
                        user_teams.append({"Id": m.team_id, "Name": f"Team {m.team_id}"})
                
                if user_teams:
                    team_id = user_teams[0]["Id"]
                    click.echo(f"Auto-detected team: {user_teams[0]['Name']} (ID: {team_id})")
                else:
                    click.echo(
                        "Error: ownership=team but no team found and --team-id not specified",
                        err=True,
                    )
                    sys.exit(1)
        except ApiException as e:
            logger.error("Stack operation failed: %s\n%s", e, traceback.format_exc())
            click.echo(f"Error: Failed to get user teams: {e}", err=True)
            sys.exit(1)

    stack_content = stack_file.read_text()
    env_vars = load_stack_env_file(env_file)

    click.echo(f"Portainer URL: {portainer_url}")
    click.echo(f"Stack Name: {stack_name}")
    click.echo(f"Stack File: {stack_file}")
    click.echo(f"Endpoint ID: {endpoint_id}")
    click.echo(f"Environment Variables: {len(env_vars)} loaded")
    if ownership:
        click.echo(f"Ownership: {ownership}")
        if ownership == "team":
            click.echo(f"Team ID: {team_id}")
    click.echo()

    try:
        with get_portainer_api_client(portainer_url, access_token) as client:
            stacks_api = StacksApi(client)
            users_api = UsersApi(client)
            rc_api = ResourceControlsApi(client)

            # Check if stack exists
            click.echo("Checking if stack already exists...")
            existing_stack_id = None
            stacks = stacks_api.stack_list()
            for stack in stacks:
                if stack.name == stack_name:
                    existing_stack_id = stack.id
                    break

            if existing_stack_id is not None:
                # Update existing stack
                click.echo(f"Updating existing stack: {stack_name} (ID: {existing_stack_id})...")
                payload = StacksUpdateSwarmStackPayload(
                    stack_file_content=stack_content,
                    env=env_vars,
                    prune=True,
                    pull_image=True,
                )
                response = stacks_api.stack_update(
                    id=existing_stack_id, endpoint_id=endpoint_id, body=payload.to_dict()
                )
                click.echo("Stack updated successfully!")
                click.echo(json.dumps(response.to_dict(), indent=2))
            else:
                # Create new stack - need swarm ID first
                click.echo("Getting swarm ID...")
                docker_client = get_portainer_docker_client(portainer_url, access_token, endpoint_id)
                swarm_info = docker_client.swarm.attrs
                swarm_id = swarm_info.get("ID") if swarm_info else None
                if not swarm_id:
                    raise StackError("Could not get swarm ID from endpoint")
                click.echo(f"Swarm ID: {swarm_id}")

                click.echo(f"Creating new stack: {stack_name}...")
                payload = StacksSwarmStackFromFileContentPayload(
                    name=stack_name,
                    stack_file_content=stack_content,
                    env=env_vars,
                    swarm_id=swarm_id,
                )
                response = stacks_api.stack_create_docker_swarm_string(
                    endpoint_id=endpoint_id, body=payload.to_dict()
                )
                click.echo("Stack created successfully!")
                click.echo(json.dumps(response.to_dict(), indent=2))

            # Apply access control
            if ownership:
                click.echo()
                
                # Get final stack ID
                final_stack_id = None
                stacks = stacks_api.stack_list()
                for stack in stacks:
                    if stack.name == stack_name:
                        final_stack_id = stack.id
                        break

                if final_stack_id:
                    stack_info = stacks_api.stack_inspect(id=final_stack_id)
                    rc = stack_info.resource_control

                    if ownership == "private":
                        if rc and rc.id:
                            user = users_api.current_user_inspect()
                            user_id = user.id
                            click.echo("Setting access control to private...")
                            rc_payload = ResourcecontrolsResourceControlUpdatePayload(
                                public=False,
                                teams=[],
                                users=[user_id],
                            )
                            rc_api.resource_control_update(id=rc.id, body=rc_payload.to_dict())
                            click.echo("✓ Access control set to private")

                    elif ownership == "team" and team_id:
                        click.echo(f"Setting access control for team {team_id}...")
                        if rc and rc.id:
                            rc_payload = ResourcecontrolsResourceControlUpdatePayload(
                                public=False,
                                teams=[team_id],
                                users=[],
                            )
                            rc_api.resource_control_update(id=rc.id, body=rc_payload.to_dict())
                            click.echo(f"✓ Access control set to team {team_id}")
                        else:
                            rc_payload = ResourcecontrolsResourceControlCreatePayload(
                                resource_id=str(final_stack_id),
                                type=PortainerResourceControlType.StackResourceControl,
                                public=False,
                                teams=[team_id],
                                users=[],
                            )
                            rc_api.resource_control_create(body=rc_payload.to_dict())
                            click.echo(f"✓ Access control created for team {team_id}")

                    elif ownership == "public":
                        click.echo("Setting access control to public...")
                        if rc and rc.id:
                            rc_payload = ResourcecontrolsResourceControlUpdatePayload(
                                public=True,
                                teams=[],
                                users=[],
                            )
                            rc_api.resource_control_update(id=rc.id, body=rc_payload.to_dict())
                            click.echo("✓ Access control set to public")
                        else:
                            rc_payload = ResourcecontrolsResourceControlCreatePayload(
                                resource_id=str(final_stack_id),
                                type=PortainerResourceControlType.StackResourceControl,
                                public=True,
                                teams=[],
                                users=[],
                            )
                            rc_api.resource_control_create(body=rc_payload.to_dict())
                            click.echo("✓ Access control created as public")

        click.echo()
        click.echo("Done!")
        sys.exit(0)

    except ApiException as e:
        error_msg = str(e.body) if e.body else str(e.reason)
        logger.error("Stack operation failed: %s\n%s", error_msg, traceback.format_exc())
        click.echo(f"Error: {error_msg}", err=True)
        click.echo()
        click.echo("Failed!")
        sys.exit(1)
    except (StackError, PortainerError) as e:
        logger.error("Stack operation failed: %s\n%s", e, traceback.format_exc())
        click.echo(f"Error: {e}", err=True)
        click.echo()
        click.echo("Failed!")
        sys.exit(1)
