from __future__ import annotations

from types import SimpleNamespace

from click.testing import CliRunner

from ptctools import clean


class _ApiClientContext:
    def __enter__(self):
        return object()

    def __exit__(self, exc_type, exc, tb):
        return False


def test_clean_uses_deserialized_image_list(monkeypatch) -> None:
    docker_client = SimpleNamespace(
        containers=SimpleNamespace(list=lambda *args, **kwargs: []),
    )

    class FakeDockerApi:
        def __init__(self, api_client):
            self.api_client = api_client

        def docker_images_list(self, environment_id: int, with_usage: bool):
            return SimpleNamespace(data=[])

    monkeypatch.setattr(clean, "get_portainer_docker_client", lambda *args: docker_client)
    monkeypatch.setattr(clean, "get_portainer_api_client", lambda *args: _ApiClientContext())
    monkeypatch.setattr(clean, "DockerApi", FakeDockerApi)

    result = CliRunner().invoke(
        clean.cli,
        ["--url", "https://portainer.example.com", "--endpoint-id", "1", "--yes"],
        env={"PORTAINER_ACCESS_TOKEN": "token"},
    )

    assert result.exit_code == 0
    assert "Nothing to clean up." in result.output
