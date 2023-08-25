"""Application settings and configuration."""


from typing import Literal, Optional

import pydantic
import pydantic_settings


_api_prefix = pydantic.constr(
    strip_whitespace=True,
    pattern=r"^$|^\/[a-zA-Z0-9\-\.\_\~]+$",
)


class OpenApiInfo(pydantic_settings.BaseSettings):
    """OpenAPI Info object.

    Attributes:
        title: The title of the API.
        description: A description of the API. Accepts CommonMark syntax.
        summary: A short summary of the API.
    """

    title: str = "Cosmos"
    description: Optional[str] = None
    summary: Optional[str] = "A system for processing, storing, and sharing data"


class Settings(pydantic_settings.BaseSettings):
    """Root application settings.

    Attributes:
        api_prefix: The URL path prefix.
        cors_origins: A JSON-formatted array of strings containing trusted URLs.
        env: The operating environment of the application.
        openapi: An instance of OpenApiInfo.
        sqlalchemy_uri: A Postgres DSN.
    """

    model_config = pydantic_settings.SettingsConfigDict(
        env_prefix="COSMOS_",
        env_nested_delimiter="__",
    )

    api_prefix: _api_prefix = "/api"
    cors_origins: list[pydantic.AnyHttpUrl] = []
    env: Literal["dev", "prod"] = "dev"
    openapi: OpenApiInfo = OpenApiInfo()
    sqlalchemy_uri: pydantic.PostgresDsn | Literal[
        "sqlite:///cosmos.db"
    ] = "sqlite:///cosmos.db"


settings = Settings()
