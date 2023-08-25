"""Application entrypoint."""


import fastapi
from fastapi.middleware import cors

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

    if config.settings.cors_origins:
        app.add_middleware(
            cors.CORSMiddleware,
            allow_credentials=True,
            allow_headers=["*"],
            allow_methods=["*"],
            allow_origins=[str(origin) for origin in config.settings.cors_origins],
        )

    return app
