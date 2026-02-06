# CLAUDE.md - ptctools

## Overview

Portainer Client Tools CLI package for managing Portainer stacks, volumes, and databases from the command line.

## Project Structure

```text
src/ptctools/
├── pyproject.toml          # Package config, entry point: ptctools.cli:main
├── README.md               # User documentation
└── src/ptctools/
    ├── __init__.py         # Version: 0.1.1
    ├── cli.py              # Main click CLI, registers docker + utils groups
    ├── docker.py           # Docker command group (registers stack, secret, config, volume, db)
    ├── _portainer.py       # Shared Portainer API utilities (internal)
    ├── _s3.py              # Shared S3/URI parsing utilities (internal)
    ├── stack.py            # docker stack deploy command (Swarm-only)
    ├── secret.py           # docker secret create command (Swarm-only)
    ├── config.py           # docker config set/get/list/delete commands (Swarm-only)
    ├── volume.py           # docker volume backup/restore/cp/rm/rename commands
    ├── db.py               # docker db backup/restore commands
    └── utils.py            # utils backup/restore commands (local Duplicati)
```

## CLI Architecture

Uses [click](https://click.palletsprojects.com/) with nested command groups:

```
ptctools
├── docker                    # Docker commands (via Portainer Docker proxy)
│   ├── stack deploy         # Deploy/update stack (Swarm-only)
│   ├── secret create        # Create Docker secret (Swarm-only)
│   ├── config set/get/list/delete  # Manage configs (Swarm-only)
│   ├── volume backup        # Backup volumes to S3 via Duplicati
│   ├── volume restore       # Restore single volume from S3
│   ├── volume cp            # Copy between volumes and S3
│   ├── volume rm            # Remove volume
│   ├── volume rename        # Rename volume (copy + delete)
│   ├── db backup            # Backup PostgreSQL via container exec
│   └── db restore           # Restore PostgreSQL from backup
├── utils backup             # Local backup to S3 or directory using Duplicati
├── utils restore            # Local restore from S3 or directory using Duplicati
└── k8s ...                  # Kubernetes commands (future)
```

## Environment Variables

All docker commands require `PORTAINER_ACCESS_TOKEN`. Backup commands also use:
- `S3_ACCESS_KEY`, `S3_SECRET_KEY` - S3 credentials
- `DUPLICATI_PASSPHRASE` - Optional encryption

## Development

```bash
# Install in development mode
uv tool install . --force

# Test CLI
ptctools --help
ptctools docker --help
```

## Adding New Commands

### Adding a Docker subcommand
1. Create module in `src/ptctools/` with a `cli` click group
2. Register in `docker.py` via `cli.add_command(module.cli, name="name")`
3. Use `_portainer.py` for Portainer API calls

### Adding a new top-level group (e.g., k8s)
1. Create module in `src/ptctools/` with a `cli` click group
2. Register in `cli.py` via `main.add_command(module.cli, name="name")`
