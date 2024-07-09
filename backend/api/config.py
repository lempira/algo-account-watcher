"""Configuration settings for the API."""

from __future__ import annotations

import json
import logging
import os
from functools import lru_cache

from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    """Configuration settings for the API."""

    environment: str = "dev"
    testing: bool = bool(0)
    allowable_origins: list[str] = ["*"]
    database_url: str = "sqlite://:memory:"


@lru_cache
def get_settings() -> BaseSettings:
    """Get the configuration settings."""
    log.info("Loading config settings from the environment...")
    database_url = os.getenv("DATABASE_URL", "sqlite://:memory:")
    allowable_origins = os.getenv("ALLOWABLE_ORIGINS", '["*"]')
    return Settings(database_url=database_url, allowable_origins=json.loads(allowable_origins))
