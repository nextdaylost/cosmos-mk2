"""Application entrypoint."""


import fastapi

from cosmos import metadata
from cosmos.core import config


def main() -> fastapi.FastAPI:
    """Application factory.

    Returns:
        An initialized FastAPI application instance.
    """
    app = fastapi.FastAPI(
        description=config.settings.openapi.description,
        summary=config.settings.openapi.summary,
        title=config.settings.openapi.title,
        version=metadata.__version__,
    )

    return app
