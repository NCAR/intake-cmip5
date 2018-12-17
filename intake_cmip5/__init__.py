#!/usr/bin/env python
"""Top-level package for intake_cmip5."""
from ._version import get_versions
import intake_cmip5
from intake_cmip5 import generate_database

__version__ = get_versions()["version"]
del get_versions

__all__ = ["intake_cmip5", "generate_database"]