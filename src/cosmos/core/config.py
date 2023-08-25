"""Application settings and configuration."""


from typing import Literal, Optional

import pydantic_settings


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
        env: The operating environment of the application.
        openapi: An instance of OpenApiInfo.
    """

    model_config = pydantic_settings.SettingsConfigDict(
        env_prefix="COSMOS_",
        env_nested_delimiter="__",
    )

    env: Literal["dev", "prod"] = "dev"
    openapi: OpenApiInfo = OpenApiInfo()


settings = Settings()
