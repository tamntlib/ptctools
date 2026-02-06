"""Docker Swarm Config management commands via Portainer API."""

from __future__ import annotations

import json
import logging
import os
import sys
import traceback
from pathlib import Path

import click
import docker.errors

from ptctools._portainer import get_portainer_docker_client, PortainerError

logger = logging.getLogger(__name__)


class ConfigError(PortainerError):
    """Exception for Docker config operations."""

    pass


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
def set_config(
    url: str,
    name: str,
    data: str | None,
    file_path: Path | None,
    endpoint_id: int,
    force: bool,
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

    try:
        client = get_portainer_docker_client(portainer_url, access_token, endpoint_id)

        # Check if config already exists
        existing = None
        for config in client.configs.list():
            if config.name == name:
                existing = config
                break

        if existing:
            if not force:
                click.echo(
                    f"Error: Config '{name}' already exists. Use --force to replace.",
                    err=True,
                )
                sys.exit(1)

            # Delete existing config first (Docker doesn't support updating configs)
            click.echo(f"Removing existing config: {name}")
            existing.remove()

        click.echo(f"Creating config: {name}")
        new_config = client.configs.create(name=name, data=data.encode("utf-8"))
        click.echo(f"✓ Config '{name}' created successfully (ID: {new_config.id})")

    except docker.errors.APIError as e:
        logger.error("Config operation failed: %s\n%s", e, traceback.format_exc())
        click.echo(f"Error: {e}", err=True)
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
