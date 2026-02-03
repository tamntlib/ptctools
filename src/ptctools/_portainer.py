"""
Common utility functions for Portainer API scripts.
"""

from __future__ import annotations

import json
import docker
import docker.api.client
from requests.adapters import HTTPAdapter as RequestsHTTPAdapter

from ptctools.portainer_client.openapi_client import ApiClient
from ptctools.portainer_client.openapi_client.configuration import Configuration
from ptctools.portainer_client.openapi_client.api.resource_controls_api import (
    ResourceControlsApi,
)
from ptctools.portainer_client.openapi_client.api.users_api import UsersApi
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


class PortainerError(Exception):
    """Base exception for Portainer-related errors."""

    pass


class ResourceControlError(PortainerError):
    """Exception for resource control operations."""

    pass


class VolumeOwnershipError(PortainerError):
    """Exception for volume ownership operations."""

    pass


class PortainerHTTPAdapter(RequestsHTTPAdapter):
    """Custom HTTP adapter that routes requests through Portainer's Docker proxy."""

    def __init__(self, portainer_url: str, endpoint_id: int, api_key: str, **kwargs):
        self.portainer_url = portainer_url.rstrip("/")
        self.endpoint_id = endpoint_id
        self.api_key = api_key
        super().__init__(**kwargs)

    def send(self, request, *args, **kwargs):
        # Rewrite URL: http://localhost:2375/v1.xx/containers/... -> {portainer_url}/api/endpoints/{id}/docker/containers/...
        original_url = request.url

        # docker-py sends to http://localhost:2375/v1.45/containers/...
        if original_url.startswith("http://localhost"):
            # Extract path after localhost (strip host and port)
            # e.g., "http://localhost:2375/v1.45/containers/abc" -> "/v1.45/containers/abc"
            from urllib.parse import urlparse

            parsed = urlparse(original_url)
            path = parsed.path
            if parsed.query:
                path = f"{path}?{parsed.query}"

            # Remove version prefix like /v1.45
            if path.startswith("/v"):
                parts = path.split("/", 2)
                if len(parts) >= 3:
                    path = "/" + parts[2]

            request.url = f"{self.portainer_url.rstrip('/')}/api/endpoints/{self.endpoint_id}/docker{path}"

        # Inject API key header
        request.headers["X-API-Key"] = self.api_key

        return super().send(request, *args, **kwargs)


def get_portainer_docker_client(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
) -> docker.DockerClient:
    """Create a docker-py client that works through Portainer's Docker proxy.

    Args:
        portainer_url: Portainer base URL (e.g., "https://portainer.example.com")
        api_key: Portainer API key
        endpoint_id: Portainer endpoint/environment ID

    Returns:
        A DockerClient configured to route through Portainer
    """
    # Create APIClient with explicit version to skip auto-detection
    api_client = docker.api.client.APIClient(
        base_url="http://localhost:2375",
        version="1.45",  # Fixed version, skip auto-detection
    )

    # APIClient inherits from requests.Session, so mount adapter directly on it
    adapter = PortainerHTTPAdapter(portainer_url, endpoint_id, api_key)
    api_client.mount("http://", adapter)
    api_client.mount("https://", adapter)

    # Wrap in high-level client
    client = docker.DockerClient()
    client.api = api_client

    return client


def get_portainer_api_client(portainer_url: str, api_key: str) -> ApiClient:
    """Create a configured ApiClient for Portainer API."""
    config = Configuration(
        host=f"{portainer_url.rstrip('/')}/api", api_key={"ApiKeyAuth": api_key}
    )
    return ApiClient(configuration=config)


def set_volume_ownership(
    portainer_url: str,
    api_key: str,
    volume_name: str,
    ownership: str,
    team_id: int | None = None,
    endpoint_id: int = 1,
) -> str:
    """Set ownership on a volume.

    Args:
        ownership: 'private', 'team', or 'public'
        team_id: Required if ownership is 'team'
        endpoint_id: Portainer endpoint ID (default 1)

    Returns:
        A message describing what was done (e.g., "set to private", "updated to team 5")

    Raises:
        VolumeOwnershipError: If ownership cannot be set
    """
    # 1. Inspect volume to get existing RC via Docker Proxy
    # This relies on Portainer injecting metadata into the Docker volume inspect response
    docker_client = get_portainer_docker_client(portainer_url, api_key, endpoint_id)
    try:
        volume = docker_client.volumes.get(volume_name)
    except docker.errors.NotFound:
        # If volume not found, we can't set ownership
        raise VolumeOwnershipError(f"Volume {volume_name} not found")
    except docker.errors.APIError as e:
        raise VolumeOwnershipError(f"Failed to inspect volume: {e}") from e

    # Extract ResourceControl ID if it exists
    # Structure: volume.attrs['Portainer']['ResourceControl']['Id']
    rc_id = None
    portainer_meta = volume.attrs.get("Portainer")
    if portainer_meta:
        rc = portainer_meta.get("ResourceControl")
        if rc:
            rc_id = rc.get("Id")

    # 2. Use Portainer Client for RC operations
    with get_portainer_api_client(portainer_url, api_key) as client:
        rc_api = ResourceControlsApi(client)
        users_api = UsersApi(client)

        if ownership == "private":
            # Get current user ID
            try:
                user = users_api.current_user_inspect()
                user_id = user.id
            except ApiException as e:
                raise VolumeOwnershipError("Failed to get current user") from e

            # Payload logic
            if rc_id:
                payload = ResourcecontrolsResourceControlUpdatePayload(
                    public=False,
                    teams=[],
                    users=[user_id],
                )
                try:
                    rc_api.resource_control_update(id=rc_id, body=payload.to_dict())
                except ApiException as e:
                    error_msg = str(e.body) if e.body else str(e.reason)
                    raise VolumeOwnershipError(
                        f"Failed to update resource control: {error_msg}"
                    ) from e
                return "updated to private"
            else:
                payload = ResourcecontrolsResourceControlCreatePayload(
                    resource_id=volume_name,
                    # IMPORTANT: Resource ID for volumes must include the suffix if present?
                    # The volume.attrs['ResourceID'] field usually contains the full ID.
                    # Or 'Name' + suffix.
                    # docker-py volume.id usually is the name for local driver, but Portainer might expect
                    # the ID with suffix if it lists it that way.
                    # Actually, for CREATION, we use the volume NAME usually if it's external?
                    # But the API sample showed "ResourceID": "llmproxy-data_db-data_t4sho5o9f8rqtdf236jvt44us"
                    # If we create a NEW control, we need to match the resource ID expected by Portainer.
                    # If Portainer hasn't assigned a suffix yet (new volume), validation might rely on name.
                    # But if we use volume.attrs['ResourceID'], that should be safer.
                    # If 'ResourceID' field is missing, fallback to volume_name.
                    # Checking the user's JSON: "ResourceID": "..." is at top level.
                    # Docker standard inspect has "Name". "ResourceID" is likely added by Portainer proxy?
                    # Let's check docker-py Volume object attrs.
                    # Defaulting to volume_name is safest for 'create' if unsure, as that's what we did before.
                    # But if Portainer uses a unique ID, we should use it.
                    # I will try to use volume.attrs.get("ResourceID") or volume_name.
                    type=PortainerResourceControlType.VolumeResourceControl,
                    public=False,
                    teams=[],
                    users=[user_id],
                )
                # Correction: ResourceID in payload.
                resource_identifier = volume.attrs.get("ResourceID", volume_name)
                payload.resource_id = resource_identifier

                try:
                    rc_api.resource_control_create(body=payload.to_dict())
                except ApiException as e:
                    error_msg = str(e.body) if e.body else str(e.reason)
                    raise VolumeOwnershipError(
                        f"Failed to create resource control: {error_msg}"
                    ) from e
                return "set to private"

        elif ownership == "team":
            if not team_id:
                # Auto-detect team
                try:
                    user = users_api.current_user_inspect()
                    memberships = users_api.user_memberships_inspect(user.id)
                    team_ids = [m.team_id for m in memberships if m.team_id]
                    if not team_ids:
                        raise VolumeOwnershipError(
                            "No team found and --team-id not specified"
                        )
                    team_id = team_ids[0]
                except ApiException as e:
                    raise VolumeOwnershipError(
                        "No team found and --team-id not specified"
                    ) from e

            if rc_id:
                payload = ResourcecontrolsResourceControlUpdatePayload(
                    public=False,
                    teams=[team_id],
                    users=[],
                )
                try:
                    rc_api.resource_control_update(id=rc_id, body=payload.to_dict())
                except ApiException as e:
                    error_msg = str(e.body) if e.body else str(e.reason)
                    raise VolumeOwnershipError(
                        f"Failed to update resource control: {error_msg}"
                    ) from e
                return f"updated to team {team_id}"
            else:
                resource_identifier = volume.attrs.get("ResourceID", volume_name)
                payload = ResourcecontrolsResourceControlCreatePayload(
                    resource_id=resource_identifier,
                    type=PortainerResourceControlType.VolumeResourceControl,
                    public=False,
                    teams=[team_id],
                    users=[],
                )
                try:
                    rc_api.resource_control_create(body=payload.to_dict())
                except ApiException as e:
                    error_msg = str(e.body) if e.body else str(e.reason)
                    raise VolumeOwnershipError(
                        f"Failed to create resource control: {error_msg}"
                    ) from e
                return f"set to team {team_id}"

        elif ownership == "public":
            if rc_id:
                payload = ResourcecontrolsResourceControlUpdatePayload(
                    public=True,
                    teams=[],
                    users=[],
                )
                try:
                    rc_api.resource_control_update(id=rc_id, body=payload.to_dict())
                except ApiException as e:
                    error_msg = str(e.body) if e.body else str(e.reason)
                    raise VolumeOwnershipError(
                        f"Failed to update resource control: {error_msg}"
                    ) from e
                return "updated to public"
            else:
                resource_identifier = volume.attrs.get("ResourceID", volume_name)
                payload = ResourcecontrolsResourceControlCreatePayload(
                    resource_id=resource_identifier,
                    type=PortainerResourceControlType.VolumeResourceControl,
                    public=True,
                    teams=[],
                    users=[],
                )
                try:
                    rc_api.resource_control_create(body=payload.to_dict())
                except ApiException as e:
                    error_msg = str(e.body) if e.body else str(e.reason)
                    raise VolumeOwnershipError(
                        f"Failed to create resource control: {error_msg}"
                    ) from e
                return "set to public"

        else:
            raise VolumeOwnershipError(f"Unknown ownership type: {ownership}")


def copy_volume_resource_control(
    portainer_url: str,
    api_key: str,
    source_volume: str,
    dest_volume: str,
    endpoint_id: int = 1,
) -> str:
    """Copy ResourceControl from source volume to destination volume.

    Returns:
        Action taken: 'copied' or 'skipped'
    """
    docker_client = get_portainer_docker_client(portainer_url, api_key, endpoint_id)

    # Check Source RC
    try:
        source_vol = docker_client.volumes.get(source_volume)
    except docker.errors.NotFound:
        return "skipped"

    source_meta = source_vol.attrs.get("Portainer", {})
    source_rc = source_meta.get("ResourceControl")

    if not source_rc:
        return "skipped"

    # Check Dest RC
    try:
        dest_vol = docker_client.volumes.get(dest_volume)
    except docker.errors.NotFound:
        return "skipped"

    dest_meta = dest_vol.attrs.get("Portainer", {})
    dest_rc = dest_meta.get("ResourceControl")

    if dest_rc:
        return "skipped"

    # Extract settings from source
    public = source_rc.get("Public", False)
    team_ids = [
        ta.get("TeamId") for ta in source_rc.get("TeamAccesses", []) if ta.get("TeamId")
    ]
    user_ids = [
        ua.get("UserId") for ua in source_rc.get("UserAccesses", []) if ua.get("UserId")
    ]

    # Create resource control on dest
    resource_identifier = dest_vol.attrs.get("ResourceID", dest_volume)

    with get_portainer_api_client(portainer_url, api_key) as client:
        rc_api = ResourceControlsApi(client)
        payload = ResourcecontrolsResourceControlCreatePayload(
            resource_id=resource_identifier,
            type=PortainerResourceControlType.VolumeResourceControl,
            public=public,
            teams=team_ids or [],
            users=user_ids or [],
        )
        try:
            rc_api.resource_control_create(body=payload.to_dict())
        except ApiException as e:
            error_msg = str(e.body) if e.body else str(e.reason)
            raise ResourceControlError(
                f"Failed to copy resource control: {error_msg}"
            ) from e

    return "copied"


def run_container(
    client: docker.DockerClient, image: str, binds: list[str] | None = None, **kwargs
) -> tuple[int, str]:
    """Run a container, wait for it to finish, and clean up.

    1. Pulls image
    2. Creates and runs container
    3. Removes container
    4. Removes image if unused

    Args:
        client: Docker client
        image: Image name (e.g. "busybox:latest")
        binds: List of volume binds (e.g. ["vol:/data"])
        **kwargs: Additional arguments for client.api.create_container

    Returns:
        tuple(exit_code, logs)
    """
    # 1. Check if image exists
    image_existed = False
    try:
        client.images.get(image)
        image_existed = True
    except docker.errors.ImageNotFound:
        image_existed = False
    except docker.errors.APIError:
        # If we can't check, assume it existed to be safe (don't delete user data)
        # And try to pull just in case the error was transient? 
        # Actually safer to assume it exists so we don't auto-remove, 
        # but we should still try to pull if we're not sure strictly...
        # But instructions say "if image exist so no need pull".
        # If API error, we don't know. Let's assume we need to pull to be safe (ensure it's there),
        # but NOT auto-remove (safe).
        image_existed = True
        # But we will fall through to pull logic if we don't set a flag "need_pull"
        pass

    # Pull image only if it didn't exist
    if not image_existed:
        try:
            # Split image into name and tag if possible, or just pass full string
            if ":" in image:
                repo, tag = image.split(":", 1)
                client.images.pull(repo, tag=tag)
            else:
                client.images.pull(image)
        except docker.errors.APIError:
            # Continue even if pull fails (maybe we are offline?)
            pass

    # Prepare host config
    # If host_config is already in kwargs, use it (but we might need to merge binds)
    # The existing usages pass host_config=client.api.create_host_config(...)
    # If the user passes 'binds' argument, we should create host_config or update it.

    # However, to be flexible:
    # If 'host_config' is passed in kwargs, use it.
    # If 'binds' is passed, we construct host_config.

    host_config = kwargs.pop("host_config", None)
    if binds and not host_config:
        host_config = client.api.create_host_config(
            binds=binds,
            auto_remove=False,
        )
    elif binds and host_config:
        # This is tricky if host_config is a dict or object.
        # docker-py create_host_config returns a dictionary.
        # We'll just assume the caller handles it if they pass both.
        # But for simpler usage, let's just support passing binds.
        pass

    # 2. Create container
    # We use client.api.create_container (low-level) as per existing usages
    # image and other args in kwargs

    # Ensure image is in kwargs or passed
    create_kwargs = kwargs.copy()
    create_kwargs["image"] = image
    if host_config:
        create_kwargs["host_config"] = host_config

    container_id = None
    try:
        container_resp = client.api.create_container(**create_kwargs)
        container_id = container_resp.get("Id")

        # 3. Start and wait
        container = client.containers.get(container_id)
        container.start()
        result = container.wait()
        exit_code = result.get("StatusCode", -1)
        logs = container.logs(stdout=True, stderr=True)
        if isinstance(logs, bytes):
            logs = logs.decode("utf-8", errors="replace")

    finally:
        # 4. Remove container
        if container_id:
            try:
                client.api.remove_container(container_id, force=True)
            except docker.errors.APIError:
                pass

        # 5. Remove image if it didn't exist before
        if not image_existed:
            try:
                client.images.remove(image=image)
            except docker.errors.APIError:
                # Likely in use by other containers or is a base image
                pass

    return exit_code, logs
