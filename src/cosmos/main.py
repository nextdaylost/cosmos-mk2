"""Application entrypoint."""


import fastapi
from fastapi.middleware import cors

from cosmos import metadata
from cosmos.api.v1 import api
from cosmos.core import config
from cosmos.db import init
from cosmos.utils.endpoints import ping


def main() -> fastapi.FastAPI:
    """Application factory.

    Returns:
        An initialized FastAPI application instance.
    """
    app = fastapi.FastAPI(
        description=config.settings.openapi.description,
        openapi_url=f"{config.settings.api_prefix}/openapi.json",
        summary=config.settings.openapi.summary,
        title=config.settings.openapi.title,
        version=metadata.__version__,
    )

    if config.settings.env == "dev":
        init.initialize_db()

    if config.settings.cors_origins:
        app.add_middleware(
            cors.CORSMiddleware,
            allow_credentials=True,
            allow_headers=["*"],
            allow_methods=["*"],
            allow_origins=[str(origin) for origin in config.settings.cors_origins],
        )

    router = fastapi.APIRouter(prefix=config.settings.api_prefix)

    router.include_router(api.router)
    router.include_router(ping.router)

    app.include_router(router)

    return app
