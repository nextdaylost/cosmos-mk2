"""Application entrypoint."""


import fastapi


def main() -> fastapi.FastAPI:
    """Application factory.

    Returns:
        An initialized FastAPI application instance.
    """
    app = fastapi.FastAPI()

    return app
