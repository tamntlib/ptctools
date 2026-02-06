"""Main CLI entry point for ptctools."""

import click

from ptctools import __version__
from ptctools import docker
from ptctools import utils


@click.group()
@click.version_option(version=__version__)
def main():
    """Portainer Client Tools - manage stacks, volumes, and databases."""
    pass


# Docker commands (via Portainer Docker proxy)
main.add_command(docker.cli, name="docker")

# Local utility commands (no Portainer needed)
main.add_command(utils.cli, name="utils")


if __name__ == "__main__":
    main()
