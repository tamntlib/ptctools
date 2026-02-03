"""Volume backup and restore commands."""

from __future__ import annotations

import logging
import os
import sys
import traceback

import click
import docker

from ptctools._portainer import (
    get_portainer_docker_client,
    copy_volume_resource_control,
    set_volume_ownership,
    run_container,
    PortainerError,
    ResourceControlError,
    VolumeOwnershipError,
)
from ptctools._s3 import (
    parse_s3_uri,
    get_s3_endpoint,
    get_s3_credentials,
    build_duplicati_s3_url,
)

logger = logging.getLogger(__name__)


class VolumeError(PortainerError):
    """Exception for volume operations."""
    pass


def backup_volume(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    volume_name: str,
    s3_endpoint: str,
    s3_bucket: str,
    s3_access_key: str,
    s3_secret_key: str,
    keep_versions: int,
    passphrase: str,
) -> None:
    """Backup a single volume to S3 using Duplicati CLI.
    
    Raises:
        VolumeError: If backup fails
    """
    s3_dest = build_duplicati_s3_url(s3_bucket, volume_name, s3_endpoint)

    click.echo(f"Backing up {volume_name} using Duplicati...")

    # Common options for both repair and backup
    common_opts = " ".join([
        f"--aws-access-key-id={s3_access_key}",
        f"--aws-secret-access-key={s3_secret_key}",
        f"--passphrase={passphrase}" if passphrase else "--no-encryption",
        "--dbpath=/tmp/duplicati.sqlite",
    ])

    # Repair command to rebuild local database from remote
    repair_cmd = f"duplicati-cli repair '{s3_dest}' {common_opts}"

    # Backup command
    backup_cmd = " ".join([
        "duplicati-cli",
        "backup",
        f"'{s3_dest}'",
        "/data",
        common_opts,
        f"--keep-versions={keep_versions}",
        "--retention-policy=",
    ])

    # Run repair first (rebuilds local DB from remote), then backup
    # Use ; instead of && because repair may return non-zero for warnings
    full_cmd = f"{repair_cmd}; {backup_cmd}"

    try:
        client = get_portainer_docker_client(portainer_url, api_key, endpoint_id)
        
        # Pull image
        # check if image unused then remove image handled by run_container
        
        # Run container
        exit_code, logs = run_container(
            client=client,
            image="duplicati/duplicati:latest",
            entrypoint=["/bin/sh", "-c"],
            command=[full_cmd],
            binds=[f"{volume_name}:/data:ro"],
        )

    except docker.errors.APIError as e:
        click.echo(f"  ✗ Backup failed: {e}")
        raise VolumeError(f"Backup failed: {e}") from e

    # Check for backup failure
    # Exit code 1 with "0 files need to be examined" = success (no changes)
    no_changes = exit_code == 1 and logs and "0 files need to be examined" in logs
    if exit_code != 0 and not no_changes:
        click.echo(f"  ✗ Backup failed with exit code {exit_code}")
        if logs:
            click.echo(f"  Logs: {logs}")
        raise VolumeError(f"Backup failed with exit code {exit_code}")

    click.echo(f"  ✓ Backup completed: s3://{s3_bucket}/{volume_name}")
    if logs:
        for line in logs.split("\n"):
            if any(
                k in line.lower()
                for k in ["uploaded", "added", "deleted", "modified", "examined"]
            ):
                click.echo(f"    {line.strip()}")


def restore_volume(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    volume_name: str,
    s3_endpoint: str,
    s3_bucket: str,
    s3_path: str,
    s3_access_key: str,
    s3_secret_key: str,
    passphrase: str,
    version: int | None,
    restore_time: str | None,
) -> None:
    """Restore a single volume from S3 using Duplicati CLI.
    
    Args:
        s3_path: S3 path to restore from (used directly, no modification).
    
    Raises:
        VolumeError: If restore fails
    """
    s3_dest = build_duplicati_s3_url(s3_bucket, s3_path, s3_endpoint)

    click.echo(f"Restoring {volume_name} using Duplicati...")

    restore_cmd = [
        "duplicati-cli",
        "restore",
        s3_dest,
        "/data/",
        f"--aws-access-key-id={s3_access_key}",
        f"--aws-secret-access-key={s3_secret_key}",
        f"--passphrase={passphrase}",
        "--overwrite=true",
        "--dbpath=/tmp/duplicati.sqlite",
        "--no-encryption" if not passphrase else "",
    ]

    if version is not None:
        restore_cmd.append(f"--version={version}")
    if restore_time:
        restore_cmd.append(f"--time={restore_time}")

    restore_cmd = [c for c in restore_cmd if c]

    try:
        client = get_portainer_docker_client(portainer_url, api_key, endpoint_id)
        
        # Run container
        exit_code, logs = run_container(
            client=client,
            image="duplicati/duplicati:latest",
            command=restore_cmd,
            binds=[f"{volume_name}:/data"],
        )

    except docker.errors.APIError as e:
        click.echo(f"  ✗ Restore failed: {e}")
        raise VolumeError(f"Restore failed: {e}") from e

    # Success if exit_code == 0, or exit_code == 2 with no files needing restore (already up-to-date)
    already_up_to_date = exit_code == 2 and logs and "0 files need to be restored" in logs
    if exit_code != 0 and not already_up_to_date:
        click.echo(f"  ✗ Restore failed with exit code {exit_code}")
        if logs:
            click.echo(f"  Logs: {logs}")
        raise VolumeError(f"Restore failed with exit code {exit_code}")

    click.echo(f"  ✓ Restore completed from s3://{s3_bucket}/{volume_name}")
    if logs:
        for line in logs.split("\n"):
            if any(
                k in line.lower() for k in ["restored", "downloaded", "files", "bytes"]
            ):
                click.echo(f"    {line.strip()}")


@click.group()
def cli():
    """Volume backup and restore commands."""
    pass


@cli.command()
@click.option("--url", "-u", required=True, help="Portainer base URL")
@click.option(
    "--volumes", "-v", required=True, help="Comma-separated list of volume names"
)
@click.option(
    "--output",
    "-o",
    required=True,
    help="S3 URI (e.g., s3://bucket or s3://endpoint/bucket)",
)
@click.option("--s3-endpoint", help="S3/MinIO endpoint URL (or S3_ENDPOINT env var)")
@click.option("--endpoint-id", "-e", type=int, default=1, help="Portainer endpoint ID")
@click.option(
    "--keep-versions", type=int, default=7, help="Keep N versions of backups"
)
@click.option("--passphrase", type=str, default="", help="Encryption passphrase")
def backup(
    url: str,
    volumes: str,
    output: str,
    s3_endpoint: str | None,
    endpoint_id: int,
    keep_versions: int,
    passphrase: str,
):
    """Backup Docker volumes to S3 using Duplicati."""
    access_token = os.environ.get("PORTAINER_ACCESS_TOKEN")
    if not access_token:
        click.echo("Error: Missing PORTAINER_ACCESS_TOKEN", err=True)
        sys.exit(1)

    try:
        s3_access_key, s3_secret_key = get_s3_credentials()
    except click.ClickException as e:
        click.echo(f"Error: {e.message}", err=True)
        sys.exit(1)

    # Parse S3 URI
    try:
        uri_endpoint, s3_bucket, _ = parse_s3_uri(output)
        endpoint = get_s3_endpoint(uri_endpoint, s3_endpoint)
    except click.ClickException as e:
        click.echo(f"Error: {e.message}", err=True)
        sys.exit(1)

    passphrase = passphrase or os.environ.get("DUPLICATI_PASSPHRASE", "")
    portainer_url = url.rstrip("/")
    volume_list = [v.strip() for v in volumes.split(",")]

    click.echo(f"Portainer URL: {portainer_url}")
    click.echo(f"S3 Endpoint: {endpoint}")
    click.echo(f"S3 Bucket: {s3_bucket}")
    click.echo(f"Volumes: {len(volume_list)}")
    click.echo(f"Keep Versions: {keep_versions}")
    click.echo(f"Encryption: {'Enabled' if passphrase else 'Disabled'}")
    click.echo()
    click.echo("=== Backing up volumes with Duplicati ===")

    success_count = 0
    for vol in volume_list:
        try:
            backup_volume(
                portainer_url,
                access_token,
                endpoint_id,
                vol,
                endpoint,
                s3_bucket,
                s3_access_key,
                s3_secret_key,
                keep_versions,
                passphrase,
            )
            success_count += 1
        except VolumeError as e:
            logger.error("Volume backup failed for '%s': %s\n%s", vol, e, traceback.format_exc())
        click.echo()

    click.echo("=== Volume backup complete ===")
    click.echo(f"Successfully backed up {success_count}/{len(volume_list)} volumes")
    sys.exit(0 if success_count == len(volume_list) else 1)


def copy_volume(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    source_volume: str,
    dest_volume: str,
    ownership: str = "copy",
    team_id: int | None = None,
) -> None:
    """Copy data from one volume to another.
    
    Args:
        ownership: 'copy' (from source), 'private', 'team', or 'public'
        team_id: Required if ownership is 'team'
    
    Raises:
        VolumeError: If copy fails
    """
    click.echo(f"Copying {source_volume} -> {dest_volume}...")

    try:
        client = get_portainer_docker_client(portainer_url, api_key, endpoint_id)
        
        # Get source volume info for driver/labels
        try:
            source_vol = client.volumes.get(source_volume)
            source_info = source_vol.attrs
        except docker.errors.NotFound:
            click.echo(f"  ✗ Source volume '{source_volume}' not found")
            raise VolumeError(f"Source volume '{source_volume}' not found")
        
        # Check if dest volume exists, create if not
        try:
            client.volumes.get(dest_volume)
        except docker.errors.NotFound:
            click.echo(f"  Creating destination volume '{dest_volume}'...")
            driver = source_info.get("Driver", "local")
            labels = source_info.get("Labels", {})
            try:
                client.volumes.create(name=dest_volume, driver=driver, labels=labels or {})
            except docker.errors.APIError as e:
                click.echo(f"  ✗ Failed to create destination volume")
                raise VolumeError(f"Failed to create destination volume: {e}") from e
        
        # Copy data using busybox
        copy_cmd = "cp -a /source/. /dest/"
        exit_code, logs = run_container(
            client=client,
            image="busybox:latest",
            entrypoint=["/bin/sh", "-c"],
            command=[copy_cmd],
            binds=[
                f"{source_volume}:/source:ro",
                f"{dest_volume}:/dest",
            ],
        )

    except docker.errors.APIError as e:
        click.echo(f"  ✗ Copy failed: {e}")
        raise VolumeError(f"Copy failed: {e}") from e

    if exit_code != 0:
        click.echo(f"  ✗ Copy failed with exit code {exit_code}")
        if logs:
            click.echo(f"  Logs: {logs}")
        raise VolumeError(f"Copy failed with exit code {exit_code}")

    click.echo(f"  ✓ Data copied: {source_volume} -> {dest_volume}")

    # Handle permissions based on ownership setting
    if ownership == "copy":
        # Copy permissions from source
        try:
            action = copy_volume_resource_control(
                portainer_url, api_key, source_volume, dest_volume, endpoint_id
            )
            if action == "copied":
                click.echo(f"  ✓ Permissions copied from source")
            elif action == "skipped":
                click.echo(f"  ✓ Permissions preserved (destination already has permissions)")
        except ResourceControlError as e:
            click.echo(f"  ⚠ Warning: Failed to copy permissions - {e}")
    else:
        # Set explicit ownership
        try:
            msg = set_volume_ownership(
                portainer_url, api_key, dest_volume, ownership, team_id, endpoint_id
            )
            click.echo(f"  ✓ Permissions {msg}")
        except VolumeOwnershipError as e:
            click.echo(f"  ⚠ Warning: Failed to set permissions - {e}")


def copy_s3_to_volume(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    volume_name: str,
    s3_endpoint: str,
    s3_bucket: str,
    s3_path: str,
    s3_access_key: str,
    s3_secret_key: str,
) -> None:
    """Copy files from S3 to a volume using mc (MinIO Client).
    
    Raises:
        VolumeError: If copy fails
    """
    click.echo(f"Copying s3://{s3_bucket}/{s3_path} -> {volume_name}...")

    try:
        client = get_portainer_docker_client(portainer_url, api_key, endpoint_id)
        
        # Create destination volume if it doesn't exist
        try:
            client.volumes.get(volume_name)
        except docker.errors.NotFound:
            click.echo(f"  Creating destination volume '{volume_name}'...")
            try:
                client.volumes.create(name=volume_name)
            except docker.errors.APIError as e:
                click.echo(f"  ✗ Failed to create destination volume")
                raise VolumeError(f"Failed to create destination volume: {e}") from e

        # Build mc commands: configure alias and copy
        s3_source = f"s3/{s3_bucket}/{s3_path}" if s3_path else f"s3/{s3_bucket}"
        mc_cmd = " && ".join([
            f"mc alias set s3 {s3_endpoint} {s3_access_key} {s3_secret_key}",
            f"mc cp --recursive {s3_source}/ /data/",
        ])

        exit_code, logs = run_container(
            client=client,
            image="minio/mc:latest",
            entrypoint=["/bin/sh", "-c"],
            command=[mc_cmd],
            binds=[f"{volume_name}:/data"],
        )

    except docker.errors.APIError as e:
        click.echo(f"  ✗ Copy failed: {e}")
        raise VolumeError(f"Copy failed: {e}") from e

    if exit_code != 0:
        click.echo(f"  ✗ Copy failed with exit code {exit_code}")
        if logs:
            click.echo(f"  Logs: {logs}")
        raise VolumeError(f"Copy failed with exit code {exit_code}")

    click.echo(f"  ✓ Copy completed: s3://{s3_bucket}/{s3_path} -> {volume_name}")


def copy_volume_to_s3(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    volume_name: str,
    s3_endpoint: str,
    s3_bucket: str,
    s3_path: str,
    s3_access_key: str,
    s3_secret_key: str,
) -> None:
    """Copy files from a volume to S3 using mc (MinIO Client).
    
    Raises:
        VolumeError: If copy fails
    """
    click.echo(f"Copying {volume_name} -> s3://{s3_bucket}/{s3_path}...")

    try:
        client = get_portainer_docker_client(portainer_url, api_key, endpoint_id)
        
        # Build mc commands: configure alias and copy
        s3_dest = f"s3/{s3_bucket}/{s3_path}" if s3_path else f"s3/{s3_bucket}"
        mc_cmd = " && ".join([
            f"mc alias set s3 {s3_endpoint} {s3_access_key} {s3_secret_key}",
            f"mc cp --recursive /data/ {s3_dest}/",
        ])

        exit_code, logs = run_container(
            client=client,
            image="minio/mc:latest",
            entrypoint=["/bin/sh", "-c"],
            command=[mc_cmd],
            binds=[f"{volume_name}:/data:ro"],
        )

    except docker.errors.APIError as e:
        click.echo(f"  ✗ Copy failed: {e}")
        raise VolumeError(f"Copy failed: {e}") from e

    if exit_code != 0:
        click.echo(f"  ✗ Copy failed with exit code {exit_code}")
        if logs:
            click.echo(f"  Logs: {logs}")
        raise VolumeError(f"Copy failed with exit code {exit_code}")

    click.echo(f"  ✓ Copy completed: {volume_name} -> s3://{s3_bucket}/{s3_path}")


@cli.command()
@click.option("--url", "-u", required=True, help="Portainer base URL")
@click.argument("source")
@click.argument("dest")
@click.option("--endpoint-id", "-e", type=int, default=1, help="Portainer endpoint ID")
@click.option("--s3-endpoint", help="S3/MinIO endpoint URL (or S3_ENDPOINT env var)")
@click.option(
    "--ownership",
    type=click.Choice(["private", "team", "public", "copy"]),
    default="copy",
    help="Access control: copy from source (default), private, team, or public",
)
@click.option("--team-id", "-t", type=int, help="Team ID for team ownership")
def cp(
    url: str,
    source: str,
    dest: str,
    endpoint_id: int,
    s3_endpoint: str | None,
    ownership: str,
    team_id: int | None,
):
    """Copy data between volumes and S3 (raw copy).

    SOURCE and DEST can be volume names or S3 URIs.

    Examples:
        ptctools volume cp source dest
        ptctools volume cp source dest --ownership team
        ptctools volume cp source dest --ownership private
        ptctools volume cp s3://bucket/path volume_a
        ptctools volume cp volume_a s3://bucket/path
    """
    from ptctools._s3 import is_s3_uri, parse_s3_uri, get_s3_endpoint, get_s3_credentials

    access_token = os.environ.get("PORTAINER_ACCESS_TOKEN")
    if not access_token:
        click.echo("Error: Missing PORTAINER_ACCESS_TOKEN", err=True)
        sys.exit(1)

    portainer_url = url.rstrip("/")
    source_is_s3 = is_s3_uri(source)
    dest_is_s3 = is_s3_uri(dest)

    # Both are S3 - not supported
    if source_is_s3 and dest_is_s3:
        click.echo("Error: Cannot copy directly between S3 locations. Use volume as intermediate.", err=True)
        sys.exit(1)

    # Volume to Volume copy
    if not source_is_s3 and not dest_is_s3:
        click.echo(f"Portainer URL: {portainer_url}")
        click.echo(f"Source Volume: {source}")
        click.echo(f"Destination Volume: {dest}")
        click.echo()
        click.echo("=== Copying volume data ===")

        try:
            copy_volume(
                portainer_url,
                access_token,
                endpoint_id,
                source,
                dest,
                ownership,
                team_id,
            )
            click.echo()
            click.echo("=== Volume copy complete ===")
            sys.exit(0)
        except VolumeError as e:
            logger.error("Volume copy failed: %s\n%s", e, traceback.format_exc())
            click.echo()
            click.echo("=== Volume copy failed ===")
            sys.exit(1)

    # Get S3 credentials
    try:
        s3_access_key, s3_secret_key = get_s3_credentials()
    except click.ClickException as e:
        click.echo(f"Error: {e.message}", err=True)
        sys.exit(1)

    # S3 to Volume (download)
    if source_is_s3:
        try:
            uri_endpoint, s3_bucket, s3_path = parse_s3_uri(source)
            endpoint = get_s3_endpoint(uri_endpoint, s3_endpoint)
        except click.ClickException as e:
            click.echo(f"Error: {e.message}", err=True)
            sys.exit(1)

        volume_name = dest

        click.echo(f"Portainer URL: {portainer_url}")
        click.echo(f"S3 Endpoint: {endpoint}")
        click.echo(f"S3 Source: s3://{s3_bucket}/{s3_path}")
        click.echo(f"Destination Volume: {volume_name}")
        click.echo()
        click.echo("=== Copying from S3 to volume ===")

        try:
            copy_s3_to_volume(
                portainer_url,
                access_token,
                endpoint_id,
                volume_name,
                endpoint,
                s3_bucket,
                s3_path,
                s3_access_key,
                s3_secret_key,
            )
            click.echo()
            click.echo("=== Copy from S3 complete ===")
            sys.exit(0)
        except VolumeError as e:
            logger.error("S3 to volume copy failed: %s\n%s", e, traceback.format_exc())
            click.echo()
            click.echo("=== Copy from S3 failed ===")
            sys.exit(1)

    # Volume to S3 (upload)
    if dest_is_s3:
        try:
            uri_endpoint, s3_bucket, s3_path = parse_s3_uri(dest)
            endpoint = get_s3_endpoint(uri_endpoint, s3_endpoint)
        except click.ClickException as e:
            click.echo(f"Error: {e.message}", err=True)
            sys.exit(1)

        volume_name = source
        # Use s3_path if provided, otherwise use volume name
        upload_path = s3_path if s3_path else volume_name

        click.echo(f"Portainer URL: {portainer_url}")
        click.echo(f"Source Volume: {volume_name}")
        click.echo(f"S3 Endpoint: {endpoint}")
        click.echo(f"S3 Destination: s3://{s3_bucket}/{upload_path}")
        click.echo()
        click.echo("=== Copying volume to S3 ===")

        try:
            copy_volume_to_s3(
                portainer_url,
                access_token,
                endpoint_id,
                volume_name,
                endpoint,
                s3_bucket,
                upload_path,
                s3_access_key,
                s3_secret_key,
            )
            click.echo()
            click.echo("=== Copy to S3 complete ===")
            sys.exit(0)
        except VolumeError as e:
            logger.error("Volume to S3 copy failed: %s\n%s", e, traceback.format_exc())
            click.echo()
            click.echo("=== Copy to S3 failed ===")
            sys.exit(1)


@cli.command()
@click.option("--url", "-u", required=True, help="Portainer base URL")
@click.argument("volume")
@click.option("--endpoint-id", "-e", type=int, default=1, help="Portainer endpoint ID")
@click.option("--force", "-f", is_flag=True, help="Force removal even if in use")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt")
def rm(
    url: str,
    volume: str,
    endpoint_id: int,
    force: bool,
    yes: bool,
):
    """Remove a Docker volume.

    VOLUME is the volume name to remove.

    Example: ptctools volume rm volume_a
    """
    access_token = os.environ.get("PORTAINER_ACCESS_TOKEN")
    if not access_token:
        click.echo("Error: Missing PORTAINER_ACCESS_TOKEN", err=True)
        sys.exit(1)

    portainer_url = url.rstrip("/")

    if not yes:
        if not click.confirm(f"Are you sure you want to delete volume '{volume}'?"):
            click.echo("Aborted.")
            sys.exit(0)

    click.echo(f"Removing volume: {volume}...")

    try:
        client = get_portainer_docker_client(portainer_url, access_token, endpoint_id)
        vol = client.volumes.get(volume)
        vol.remove(force=force)
        click.echo(f"  ✓ Volume '{volume}' removed")
        sys.exit(0)
    except docker.errors.NotFound:
        click.echo(f"  ✓ Volume '{volume}' removed")  # Already deleted
        sys.exit(0)
    except docker.errors.APIError as e:
        logger.error("Volume removal failed: %s\n%s", e, traceback.format_exc())
        click.echo(f"  ✗ Failed to remove volume '{volume}': {e}", err=True)
        sys.exit(1)


@cli.command()
@click.option("--url", "-u", required=True, help="Portainer base URL")
@click.argument("old_name")
@click.argument("new_name")
@click.option("--endpoint-id", "-e", type=int, default=1, help="Portainer endpoint ID")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt")
def rename(
    url: str,
    old_name: str,
    new_name: str,
    endpoint_id: int,
    yes: bool,
):
    """Rename a Docker volume (copy to new, delete old).

    OLD_NAME is the current volume name.
    NEW_NAME is the new volume name.

    Example: ptctools volume rename volume_a volume_b
    """
    access_token = os.environ.get("PORTAINER_ACCESS_TOKEN")
    if not access_token:
        click.echo("Error: Missing PORTAINER_ACCESS_TOKEN", err=True)
        sys.exit(1)

    portainer_url = url.rstrip("/")

    if not yes:
        if not click.confirm(f"Rename '{old_name}' to '{new_name}'? This will copy data and delete the original."):
            click.echo("Aborted.")
            sys.exit(0)

    click.echo(f"Renaming volume: {old_name} -> {new_name}")
    click.echo()

    # Step 1: Copy data to new volume
    click.echo("Step 1: Copying data to new volume...")
    try:
        copy_volume(portainer_url, access_token, endpoint_id, old_name, new_name)
    except VolumeError as e:
        logger.error("Volume rename failed during copy: %s\n%s", e, traceback.format_exc())
        click.echo("  ✗ Failed to copy data. Original volume unchanged.", err=True)
        sys.exit(1)

    # Step 2: Delete old volume using docker-py
    click.echo()
    click.echo("Step 2: Removing old volume...")
    try:
        client = get_portainer_docker_client(portainer_url, access_token, endpoint_id)
        vol = client.volumes.get(old_name)
        vol.remove(force=True)
        click.echo(f"  ✓ Volume '{old_name}' removed")
    except docker.errors.NotFound:
        click.echo(f"  ✓ Volume '{old_name}' removed")  # Already deleted
    except docker.errors.APIError as e:
        logger.error("Volume rename failed during delete: %s\n%s", e, traceback.format_exc())
        click.echo(f"  ⚠ Warning: Failed to remove old volume '{old_name}'", err=True)
        click.echo(f"    Data has been copied to '{new_name}'. Please remove '{old_name}' manually.")
        sys.exit(1)

    click.echo()
    click.echo(f"=== Volume renamed: {old_name} -> {new_name} ===")
    sys.exit(0)


@cli.command()
@click.option("--url", "-u", required=True, help="Portainer base URL")
@click.option(
    "--volume",
    "-v",
    default=None,
    help="Volume name (derived from input URI path if not provided)",
)
@click.option(
    "--input",
    "-i",
    "input_uri",
    required=True,
    help="S3 URI (e.g., s3://bucket/volume-name or s3://endpoint/bucket/volume-name)",
)
@click.option("--s3-endpoint", help="S3/MinIO endpoint URL (or S3_ENDPOINT env var)")
@click.option("--endpoint-id", "-e", type=int, default=1, help="Portainer endpoint ID")
@click.option(
    "--version", type=int, default=None, help="Backup version to restore (0=latest)"
)
@click.option(
    "--time", "restore_time", type=str, default=None, help="Restore to specific time"
)
@click.option("--passphrase", type=str, default="", help="Encryption passphrase")
def restore(
    url: str,
    volume: str | None,
    input_uri: str,
    s3_endpoint: str | None,
    endpoint_id: int,
    version: int | None,
    restore_time: str | None,
    passphrase: str,
):
    """Restore Docker volumes from S3 using Duplicati."""
    access_token = os.environ.get("PORTAINER_ACCESS_TOKEN")
    if not access_token:
        click.echo("Error: Missing PORTAINER_ACCESS_TOKEN", err=True)
        sys.exit(1)

    try:
        s3_access_key, s3_secret_key = get_s3_credentials()
    except click.ClickException as e:
        click.echo(f"Error: {e.message}", err=True)
        sys.exit(1)

    # Parse S3 URI
    try:
        uri_endpoint, s3_bucket, uri_path = parse_s3_uri(input_uri)
        endpoint = get_s3_endpoint(uri_endpoint, s3_endpoint)
    except click.ClickException as e:
        click.echo(f"Error: {e.message}", err=True)
        sys.exit(1)

    # Get s3_path from URI (use as-is)
    s3_path = uri_path.strip("/") if uri_path else ""

    # Determine volume name: 1) from --volume arg, 2) from s3_path
    if volume:
        volume_name = volume
    elif s3_path:
        # Use the first path segment as volume name
        volume_name = s3_path.split("/")[0]
    else:
        click.echo("Error: No volume specified. Use --volume or include path in input URI", err=True)
        sys.exit(1)

    passphrase = passphrase or os.environ.get("DUPLICATI_PASSPHRASE", "")
    portainer_url = url.rstrip("/")

    click.echo(f"Portainer URL: {portainer_url}")
    click.echo(f"S3 Endpoint: {endpoint}")
    click.echo(f"S3 Bucket: {s3_bucket}")
    click.echo(f"S3 Path: {s3_path}")
    click.echo(f"Volume: {volume_name}")
    click.echo(f"Encryption: {'Enabled' if passphrase else 'Disabled'}")
    if version is not None:
        click.echo(f"Version: {version}")
    if restore_time:
        click.echo(f"Time: {restore_time}")
    click.echo()
    click.echo("=== Restoring volumes with Duplicati ===")

    try:
        restore_volume(
            portainer_url,
            access_token,
            endpoint_id,
            volume_name,
            endpoint,
            s3_bucket,
            s3_path,
            s3_access_key,
            s3_secret_key,
            passphrase,
            version,
            restore_time,
        )
        click.echo()
        click.echo("=== Volume restore complete ===")
        sys.exit(0)
    except VolumeError as e:
        logger.error("Volume restore failed: %s\n%s", e, traceback.format_exc())
        click.echo()
        click.echo("=== Volume restore failed ===")
        sys.exit(1)
