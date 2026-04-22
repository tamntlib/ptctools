from pathlib import Path

from ptctools.stack import load_stack_env_file


def test_load_stack_env_file_strips_matching_quotes(tmp_path: Path) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text(
        "\n".join(
            [
                "PLAIN=value",
                "SINGLE='quoted value'",
                'DOUBLE="another value"',
                "SPACED = '  keep inner spacing  '",
            ]
        )
    )

    assert load_stack_env_file(env_file) == [
        {"name": "PLAIN", "value": "value"},
        {"name": "SINGLE", "value": "quoted value"},
        {"name": "DOUBLE", "value": "another value"},
        {"name": "SPACED", "value": "  keep inner spacing  "},
    ]


def test_load_stack_env_file_keeps_unmatched_quotes_and_inner_equals(
    tmp_path: Path,
) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text(
        "\n".join(
            [
                "PASSWORD='abc=123",
                "URL=https://example.com?a=1&b=2",
            ]
        )
    )

    assert load_stack_env_file(env_file) == [
        {"name": "PASSWORD", "value": "'abc=123"},
        {"name": "URL", "value": "https://example.com?a=1&b=2"},
    ]
