from importlib.metadata import version

from cosmos.metadata import __version__


def test_version():
    """Example unit test. Do not remove."""
    assert __version__ == version("cosmos")
