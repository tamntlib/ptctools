from __future__ import annotations

from types import SimpleNamespace

from ptctools.config import _update_service_spec


def test_update_service_spec_preserves_rollout_settings() -> None:
    calls: list[dict] = []

    class FakeService:
        id = "svc-123"
        attrs = {"Version": {"Index": 7}}

        def reload(self) -> None:
            return None

    service = FakeService()
    client = SimpleNamespace(
        api=SimpleNamespace(
            update_service=lambda *args, **kwargs: calls.append(
                {"args": args, "kwargs": kwargs}
            )
        )
    )
    spec = {
        "TaskTemplate": {"ContainerSpec": {"Image": "example:latest"}},
        "Name": "example",
        "Mode": {"Replicated": {"Replicas": 1}},
        "Labels": {"app": "example"},
        "UpdateConfig": {"Parallelism": 2},
        "RollbackConfig": {"Parallelism": 1},
        "EndpointSpec": {"Mode": "vip"},
    }

    _update_service_spec(client, service, spec)

    assert len(calls) == 1
    kwargs = calls[0]["kwargs"]
    assert kwargs["update_config"] == spec["UpdateConfig"]
    assert kwargs["rollback_config"] == spec["RollbackConfig"]
    assert kwargs["fetch_current_spec"] is True
