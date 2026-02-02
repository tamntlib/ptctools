"""
Common utility functions for Portainer API scripts.
"""

from __future__ import annotations

import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


def api_request(
    url: str,
    api_key: str,
    method: str = "GET",
    data: dict | None = None,
) -> tuple[dict | list | None, int]:
    """Make an API request to Portainer."""
    headers = {
        "X-API-Key": api_key,
        "Content-Type": "application/json",
    }

    body = json.dumps(data).encode("utf-8") if data else None
    req = Request(url, data=body, headers=headers, method=method)

    try:
        with urlopen(req) as response:
            response_body = response.read().decode("utf-8")
            return json.loads(response_body) if response_body else None, response.status
    except HTTPError as e:
        response_body = e.read().decode("utf-8")
        try:
            return json.loads(response_body), e.code
        except json.JSONDecodeError:
            return {"error": response_body}, e.code
    except URLError as e:
        return {"error": str(e.reason)}, 0


def create_container(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    config: dict,
) -> str | None:
    """Create a container and return its ID."""
    url = f"{portainer_url}/api/endpoints/{endpoint_id}/docker/containers/create"
    response, status_code = api_request(url, api_key, method="POST", data=config)

    if 200 <= status_code < 300 and response:
        return response.get("Id")
    else:
        print(f"Error creating container (HTTP {status_code}):")
        print(json.dumps(response, indent=2))
        return None


def pull_image(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    image: str,
) -> bool:
    """Pull a Docker image."""
    from urllib.request import Request, urlopen
    from urllib.parse import quote

    url = f"{portainer_url}/api/endpoints/{endpoint_id}/docker/images/create?fromImage={quote(image)}"
    headers = {"X-API-Key": api_key}
    req = Request(url, data=b"", headers=headers, method="POST")

    try:
        with urlopen(req) as response:
            # Read streaming response (Docker sends progress updates)
            response.read()
            return response.status == 200
    except Exception:
        return False


def start_container(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    container_id: str,
) -> bool:
    """Start a container."""
    url = f"{portainer_url}/api/endpoints/{endpoint_id}/docker/containers/{container_id}/start"
    _, status_code = api_request(url, api_key, method="POST")
    return 200 <= status_code < 300


def wait_container(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    container_id: str,
) -> int:
    """Wait for a container to finish and return exit code."""
    url = f"{portainer_url}/api/endpoints/{endpoint_id}/docker/containers/{container_id}/wait"
    response, status_code = api_request(url, api_key, method="POST")

    if 200 <= status_code < 300 and response:
        return response.get("StatusCode", -1)
    return -1


def get_container_logs(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    container_id: str,
) -> str:
    """Get container logs."""
    url = f"{portainer_url}/api/endpoints/{endpoint_id}/docker/containers/{container_id}/logs?stdout=true&stderr=true"

    headers = {"X-API-Key": api_key}
    req = Request(url, headers=headers, method="GET")

    try:
        with urlopen(req) as response:
            # Docker logs have stream headers, strip them
            raw_logs = response.read()
            # Simple cleanup - remove Docker stream headers (8 bytes each)
            logs = ""
            i = 0
            while i < len(raw_logs):
                if i + 8 <= len(raw_logs):
                    size = int.from_bytes(raw_logs[i + 4 : i + 8], "big")
                    if i + 8 + size <= len(raw_logs):
                        logs += raw_logs[i + 8 : i + 8 + size].decode(
                            "utf-8", errors="replace"
                        )
                        i += 8 + size
                        continue
                break
            return logs
    except Exception as e:
        return f"Error getting logs: {e}"


def remove_container(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    container_id: str,
) -> bool:
    """Remove a container."""
    url = f"{portainer_url}/api/endpoints/{endpoint_id}/docker/containers/{container_id}?force=true"
    _, status_code = api_request(url, api_key, method="DELETE")
    return 200 <= status_code < 300


def find_container_by_name(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    name_filter: str,
) -> str | None:
    """Find a running container by name filter and return its ID."""
    url = f'{portainer_url}/api/endpoints/{endpoint_id}/docker/containers/json?filters={{"name":["{name_filter}"]}}'
    response, status_code = api_request(url, api_key)

    if 200 <= status_code < 300 and isinstance(response, list) and len(response) > 0:
        return response[0].get("Id")
    return None


def get_network_id(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    network_name: str,
) -> str | None:
    """Find a network by name and return its ID."""
    url = f'{portainer_url}/api/endpoints/{endpoint_id}/docker/networks?filters={{"name":["{network_name}"]}}'
    response, status_code = api_request(url, api_key)

    if 200 <= status_code < 300 and isinstance(response, list) and len(response) > 0:
        return response[0].get("Id")
    return None


def create_exec(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    container_id: str,
    cmd: list[str],
) -> str | None:
    """Create an exec instance in a container and return the exec ID."""
    url = f"{portainer_url}/api/endpoints/{endpoint_id}/docker/containers/{container_id}/exec"
    config = {
        "AttachStdout": True,
        "AttachStderr": True,
        "Cmd": cmd,
    }
    response, status_code = api_request(url, api_key, method="POST", data=config)

    if 200 <= status_code < 300 and response:
        return response.get("Id")
    return None


def start_exec(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    exec_id: str,
) -> tuple[int, str]:
    """Start an exec instance and return (exit_code, output)."""
    from urllib.request import Request, urlopen

    url = f"{portainer_url}/api/endpoints/{endpoint_id}/docker/exec/{exec_id}/start"
    headers = {
        "X-API-Key": api_key,
        "Content-Type": "application/json",
    }
    body = json.dumps({"Detach": False, "Tty": False}).encode("utf-8")
    req = Request(url, data=body, headers=headers, method="POST")

    try:
        with urlopen(req) as response:
            # Read raw output (has Docker stream headers like logs)
            raw_output = response.read()
            # Strip Docker stream headers
            output = ""
            i = 0
            while i < len(raw_output):
                if i + 8 <= len(raw_output):
                    size = int.from_bytes(raw_output[i + 4 : i + 8], "big")
                    if i + 8 + size <= len(raw_output):
                        output += raw_output[i + 8 : i + 8 + size].decode(
                            "utf-8", errors="replace"
                        )
                        i += 8 + size
                        continue
                break
    except Exception as e:
        return -1, f"Error: {e}"

    # Get exec exit code
    inspect_url = (
        f"{portainer_url}/api/endpoints/{endpoint_id}/docker/exec/{exec_id}/json"
    )
    inspect_resp, _ = api_request(inspect_url, api_key)
    exit_code = inspect_resp.get("ExitCode", -1) if inspect_resp else -1

    return exit_code, output


def run_ephemeral_container(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    config: dict,
    pull: bool = True,
) -> tuple[int, str]:
    """Run an ephemeral container and return (exit_code, logs)."""
    image = config.get("Image")
    if pull and image:
        if not pull_image(portainer_url, api_key, endpoint_id, image):
            print(f"Warning: Failed to pull image {image}, trying to run anyway...")

    container_id = create_container(portainer_url, api_key, endpoint_id, config)
    if not container_id:
        return -1, "Failed to create container"

    try:
        if not start_container(portainer_url, api_key, endpoint_id, container_id):
            return -1, "Failed to start container"

        exit_code = wait_container(portainer_url, api_key, endpoint_id, container_id)
        logs = get_container_logs(portainer_url, api_key, endpoint_id, container_id)

        return exit_code, logs
    finally:
        remove_container(portainer_url, api_key, endpoint_id, container_id)


def get_volume_info(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    volume_name: str,
) -> dict | None:
    """Get volume details from Portainer."""
    url = f"{portainer_url}/api/endpoints/{endpoint_id}/docker/volumes/{volume_name}"
    response, status_code = api_request(url, api_key)
    if 200 <= status_code < 300 and response:
        return response
    return None


def create_volume(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    volume_name: str,
    driver: str = "local",
    labels: dict | None = None,
) -> bool:
    """Create a Docker volume via Portainer API."""
    url = f"{portainer_url}/api/endpoints/{endpoint_id}/docker/volumes/create"
    data = {
        "Name": volume_name,
        "Driver": driver,
        "Labels": labels or {},
    }
    _, status_code = api_request(url, api_key, method="POST", data=data)
    return 200 <= status_code < 300


def delete_volume(
    portainer_url: str,
    api_key: str,
    endpoint_id: int,
    volume_name: str,
    force: bool = False,
) -> bool:
    """Delete a Docker volume via Portainer API."""
    url = f"{portainer_url}/api/endpoints/{endpoint_id}/docker/volumes/{volume_name}"
    if force:
        url += "?force=true"
    _, status_code = api_request(url, api_key, method="DELETE")
    return 200 <= status_code < 300 or status_code == 404


def get_volume_resource_control(
    portainer_url: str,
    api_key: str,
    volume_name: str,
) -> dict | None:
    """Get ResourceControl for a volume from Portainer."""
    url = f"{portainer_url}/api/resource_controls"
    response, status_code = api_request(url, api_key)
    if 200 <= status_code < 300 and isinstance(response, list):
        for rc in response:
            if rc.get("Type") == "volume" and rc.get("ResourceId") == volume_name:
                return rc
    return None


def get_current_user_id(portainer_url: str, api_key: str) -> int | None:
    """Get the current user's ID."""
    url = f"{portainer_url}/api/users/me"
    response, status_code = api_request(url, api_key)
    if 200 <= status_code < 300 and response:
        return response.get("Id")
    return None


def get_user_teams(portainer_url: str, api_key: str) -> list[dict]:
    """Get teams that the current user belongs to."""
    user_id = get_current_user_id(portainer_url, api_key)
    if not user_id:
        return []

    url = f"{portainer_url}/api/users/{user_id}/memberships"
    memberships, status_code = api_request(url, api_key)
    if status_code != 200 or not isinstance(memberships, list):
        return []

    teams = []
    for m in memberships:
        team_id = m.get("TeamID")
        if team_id:
            teams.append({"Id": team_id, "Name": f"Team {team_id}"})
    return teams


def create_volume_resource_control(
    portainer_url: str,
    api_key: str,
    volume_name: str,
    public: bool = False,
    team_ids: list[int] | None = None,
    user_ids: list[int] | None = None,
) -> tuple[bool, str]:
    """Create ResourceControl for a volume. Returns (success, message)."""
    url = f"{portainer_url}/api/resource_controls"
    data = {
        "Type": "volume",
        "ResourceID": volume_name,
        "Public": public,
        "Teams": team_ids or [],
        "Users": user_ids or [],
    }
    response, status_code = api_request(url, api_key, method="POST", data=data)
    if 200 <= status_code < 300:
        return True, "ok"
    # Extract error message from response
    error_msg = "unknown error"
    if isinstance(response, dict):
        error_msg = response.get("message") or response.get("error") or str(response)
    return False, error_msg


def update_volume_resource_control(
    portainer_url: str,
    api_key: str,
    resource_control_id: int,
    public: bool = False,
    team_ids: list[int] | None = None,
    user_ids: list[int] | None = None,
) -> tuple[bool, str]:
    """Update an existing ResourceControl. Returns (success, message)."""
    url = f"{portainer_url}/api/resource_controls/{resource_control_id}"
    data = {
        "Public": public,
        "Teams": team_ids or [],
        "Users": user_ids or [],
    }
    response, status_code = api_request(url, api_key, method="PUT", data=data)
    if 200 <= status_code < 300:
        return True, "ok"
    # Extract error message from response
    error_msg = "unknown error"
    if isinstance(response, dict):
        error_msg = response.get("message") or response.get("error") or str(response)
    return False, error_msg


def set_volume_ownership(
    portainer_url: str,
    api_key: str,
    volume_name: str,
    ownership: str,
    team_id: int | None = None,
) -> tuple[bool, str]:
    """Set ownership on a volume.
    
    Args:
        ownership: 'private', 'team', or 'public'
        team_id: Required if ownership is 'team'
    
    Returns (success, message)
    """
    # Check if volume already has resource control
    existing_rc = get_volume_resource_control(portainer_url, api_key, volume_name)
    rc_id = existing_rc.get("Id") if existing_rc else None

    if ownership == "private":
        user_id = get_current_user_id(portainer_url, api_key)
        if not user_id:
            return False, "failed to get current user"
        if rc_id:
            success, error = update_volume_resource_control(
                portainer_url, api_key, rc_id, user_ids=[user_id]
            )
            return success, "updated to private" if success else error
        else:
            success, error = create_volume_resource_control(
                portainer_url, api_key, volume_name, user_ids=[user_id]
            )
            return success, "set to private" if success else error

    elif ownership == "team":
        if not team_id:
            # Auto-detect team
            teams = get_user_teams(portainer_url, api_key)
            if not teams:
                return False, "no team found and --team-id not specified"
            team_id = teams[0]["Id"]
        if rc_id:
            success, error = update_volume_resource_control(
                portainer_url, api_key, rc_id, team_ids=[team_id]
            )
            return success, f"updated to team {team_id}" if success else error
        else:
            success, error = create_volume_resource_control(
                portainer_url, api_key, volume_name, team_ids=[team_id]
            )
            return success, f"set to team {team_id}" if success else error

    elif ownership == "public":
        if rc_id:
            success, error = update_volume_resource_control(
                portainer_url, api_key, rc_id, public=True
            )
            return success, "updated to public" if success else error
        else:
            success, error = create_volume_resource_control(
                portainer_url, api_key, volume_name, public=True
            )
            return success, "set to public" if success else error

    return False, f"unknown ownership type: {ownership}"


def copy_volume_resource_control(
    portainer_url: str,
    api_key: str,
    source_volume: str,
    dest_volume: str,
) -> tuple[bool, str]:
    """Copy ResourceControl from source volume to destination volume.
    
    Returns (success, action) where action is 'copied', 'skipped', or error message.
    Skips if destination already has permissions or source has none.
    """
    source_rc = get_volume_resource_control(portainer_url, api_key, source_volume)
    if not source_rc:
        # No resource control on source, nothing to copy
        return True, "skipped"

    # Check if destination already has permissions
    dest_rc = get_volume_resource_control(portainer_url, api_key, dest_volume)
    if dest_rc:
        # Destination already has permissions, skip
        return True, "skipped"

    # Extract settings from source
    public = source_rc.get("Public", False)
    team_ids = [ta.get("TeamId") for ta in source_rc.get("TeamAccesses", []) if ta.get("TeamId")]
    user_ids = [ua.get("UserId") for ua in source_rc.get("UserAccesses", []) if ua.get("UserId")]

    # Create resource control on destination
    success, error = create_volume_resource_control(
        portainer_url,
        api_key,
        dest_volume,
        public=public,
        team_ids=team_ids,
        user_ids=user_ids,
    )
    return success, "copied" if success else error
