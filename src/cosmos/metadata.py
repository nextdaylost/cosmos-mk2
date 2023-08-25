"""Package metadata module.

Exposes package metadata in a single canonical location, avoiding issues with
circular imports which arise from defining some metadata directly in the package
__init__.py.
"""


from importlib.metadata import version


__version__ = version("cosmos")
