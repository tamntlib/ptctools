"""Docker cleanup commands - remove exited containers and unused images."""

from __future__ import annotations

import os
import sys

import click
import docker.errors

from ptctools._portainer import (
    get_portainer_docker_client,
    get_portainer_api_client,
    PortainerError,
)
from ptctools.portainer_client.openapi_client.api.docker_api import DockerApi


class CleanError(PortainerError):
    """Exception for clean operations."""

    pass


@click.command()
@click.option(
    "--url",
    "-u",
    envvar="PORTAINER_URL",
    required=True,
    help="Portainer base URL (or PORTAINER_URL env var)",
)
@click.option("--endpoint-id", "-e", type=int, default=1, help="Portainer endpoint ID")
@click.option(
    "--yes",
    "-y",
    is_flag=True,
    default=False,
    help="Skip confirmation prompt",
)
def cli(url: str, endpoint_id: int, yes: bool):
    """Remove all exited containers and unused images.

    This command cleans up Docker resources by:
    1. Removing all containers in 'exited' state
    2. Removing all images not referenced by any container

    Example:
        ptctools docker clean
        ptctools docker clean -y  # skip confirmation
    """
    access_token = os.environ.get("PORTAINER_ACCESS_TOKEN")
    if not access_token:
        click.echo(
            "Error: Missing PORTAINER_ACCESS_TOKEN environment variable", err=True
        )
        sys.exit(1)

    portainer_url = url.rstrip("/")

    click.echo(f"Portainer URL: {portainer_url}")
    click.echo(f"Endpoint ID: {endpoint_id}")
    click.echo()

    try:
        docker_client = get_portainer_docker_client(
            portainer_url, access_token, endpoint_id
        )

        # --- Discover exited containers ---
        exited_containers = docker_client.containers.list(
            all=True, filters={"status": "exited"}
        )

        # --- Discover unused images via Portainer API ---
        with get_portainer_api_client(portainer_url, access_token) as api_client:
            docker_api = DockerApi(api_client)
            all_images = docker_api.docker_images_list(
                environment_id=endpoint_id, with_usage=True
            ).data
        unused_images = [img for img in all_images if not img.used]

        if not exited_containers and not unused_images:
            click.echo("Nothing to clean up.")
            sys.exit(0)

        # --- Show summary ---
        if exited_containers:
            click.echo(f"Exited containers ({len(exited_containers)}):")
            for c in exited_containers:
                name = c.name or c.short_id
                image = c.image.tags[0] if c.image.tags else c.attrs.get("Image", "unknown")[:20]
                click.echo(f"  - {name} ({c.short_id}) [{image}]")
            click.echo()

        if unused_images:
            click.echo(f"Unused images ({len(unused_images)}):")
            for img in unused_images:
                tags = img.tags or []
                display_tag = tags[0].split("@")[0] if tags else "<none>"
                img_id = img.id[:19]  # sha256:xxxx (first 12 hex)
                click.echo(f"  - {img_id} [{display_tag}]")
            click.echo()

        # --- Confirm ---
        if not yes:
            click.confirm("Proceed with cleanup?", abort=True)
            click.echo()

        # --- Remove exited containers ---
        removed_containers = 0
        for c in exited_containers:
            name = c.name or c.short_id
            try:
                c.remove(force=True)
                click.echo(f"  Removed container: {name} ({c.short_id})")
                removed_containers += 1
            except docker.errors.APIError as e:
                click.echo(
                    f"  Failed to remove container {name}: {e.explanation or str(e)}",
                    err=True,
                )

        if removed_containers:
            click.echo(f"Removed {removed_containers} container(s).")
            click.echo()

        # --- Remove unused images ---
        removed_images = 0
        for img in unused_images:
            tags = img.tags or []
            display_tag = tags[0].split("@")[0] if tags else img.id[:19]
            try:
                docker_client.images.remove(image=img.id, force=True)
                click.echo(f"  Removed image: {display_tag}")
                removed_images += 1
            except docker.errors.APIError as e:
                click.echo(
                    f"  Failed to remove image {display_tag}: {e.explanation or str(e)}",
                    err=True,
                )

        if removed_images:
            click.echo(f"Removed {removed_images} image(s).")
            click.echo()

        click.echo("Done!")
        sys.exit(0)

    except docker.errors.APIError as e:
        click.echo(f"Error: {e.explanation or str(e)}", err=True)
        click.echo()
        click.echo("Failed!")
        sys.exit(1)
    except CleanError as e:
        click.echo(f"Error: {e}", err=True)
        click.echo()
        click.echo("Failed!")
        sys.exit(1)
