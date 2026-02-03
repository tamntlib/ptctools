"""Portainer Client Tools - CLI for managing Portainer stacks and backups."""

__version__ = "0.1.1"

import sys
import os

# Add portainer_client to sys.path so generated openapi_client can be imported by its internal code
sys.path.append(os.path.join(os.path.dirname(__file__), "portainer_client"))
