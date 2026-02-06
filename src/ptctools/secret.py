"""Secret management commands."""

from __future__ import annotations

import base64
import os
import sys
from pathlib import Path

import click
import docker.errors

from ptctools._portainer import (
    get_portainer_docker_client,
    PortainerError,
)


class SecretError(PortainerError):
    """Exception for secret operations."""

    pass


@click.group()
def cli():
    """Secret management commands."""
    pass


@cli.command()
@click.option(
    "--url",
    "-u",
    envvar="PORTAINER_URL",
    required=True,
    help="Portainer base URL (or PORTAINER_URL env var)",
)
@click.option("--endpoint-id", "-e", type=int, default=1, help="Portainer endpoint ID")
@click.option(
    "--file",
    "-f",
    "file_path",
    type=click.Path(exists=True, path_type=Path),
    help="Read secret from file",
)
@click.option(
    "--value", "-v", help="Secret value (use stdin or --file for sensitive data)"
)
@click.argument("name")
def create(
    url: str,
    endpoint_id: int,
    file_path: Path | None,
    value: str | None,
    name: str,
):
    """Create a Docker Swarm secret.

    NAME is the name of the secret to create.

    The secret value can be provided via:
    - stdin: echo "secret" | ptctools docker secret create -u URL my_secret
    - file: ptctools docker secret create -u URL -f /path/to/file my_secret
    - value: ptctools docker secret create -u URL -v "secret" my_secret

    Example:
        echo "postgresql://user:pass@db:5432/mydb" | ptctools docker secret create -u https://portainer.example.com litellm_db_dsn
    """
    access_token = os.environ.get("PORTAINER_ACCESS_TOKEN")
    if not access_token:
        click.echo(
            "Error: Missing PORTAINER_ACCESS_TOKEN environment variable", err=True
        )
        sys.exit(1)

    # Determine secret data source
    secret_data: bytes | None = None

    if file_path:
        # Read from file
        secret_data = file_path.read_bytes()
    elif value:
        # Use provided value
        secret_data = value.encode("utf-8")
    elif not sys.stdin.isatty():
        # Read from stdin
        secret_data = sys.stdin.read().encode("utf-8")
    else:
        click.echo(
            "Error: Secret value required. Use --file, --value, or pipe via stdin.",
            err=True,
        )
        sys.exit(1)

    # Strip trailing newline if present (common when piping from echo)
    if secret_data.endswith(b"\n"):
        secret_data = secret_data.rstrip(b"\n")

    portainer_url = url.rstrip("/")

    click.echo(f"Portainer URL: {portainer_url}")
    click.echo(f"Endpoint ID: {endpoint_id}")
    click.echo(f"Secret Name: {name}")
    click.echo()

    try:
        docker_client = get_portainer_docker_client(
            portainer_url, access_token, endpoint_id
        )

        # Check if secret already exists
        try:
            existing = docker_client.secrets.get(name)
            click.echo(
                f"Error: Secret '{name}' already exists (ID: {existing.id[:12]})",
                err=True,
            )
            click.echo(
                "Use 'docker secret rm' to remove it first, or choose a different name.",
                err=True,
            )
            sys.exit(1)
        except docker.errors.NotFound:
            pass  # Good, secret doesn't exist

        # Create the secret
        click.echo(f"Creating secret '{name}'...")
        secret = docker_client.secrets.create(name=name, data=secret_data)
        click.echo(f"Secret created successfully!")
        click.echo(f"  ID: {secret.id}")
        click.echo(f"  Name: {name}")
        click.echo()
        click.echo("Done!")
        sys.exit(0)

    except docker.errors.APIError as e:
        click.echo(f"Error: {e.explanation or str(e)}", err=True)
        click.echo()
        click.echo("Failed!")
        sys.exit(1)
    except SecretError as e:
        click.echo(f"Error: {e}", err=True)
        click.echo()
        click.echo("Failed!")
        sys.exit(1)
