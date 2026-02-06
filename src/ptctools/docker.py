"""Docker management commands (via Portainer Docker proxy)."""

import click

from ptctools import stack
from ptctools import secret
from ptctools import config
from ptctools import volume
from ptctools import db


@click.group()
def cli():
    """Docker management commands.

    These commands work with Docker environments via Portainer.
    Some commands (stack, secret, config) require Docker Swarm.
    """
    pass


# Swarm-only commands
cli.add_command(stack.cli, name="stack")
cli.add_command(secret.cli, name="secret")
cli.add_command(config.cli, name="config")

# Any Docker commands
cli.add_command(volume.cli, name="volume")
cli.add_command(db.cli, name="db")
