"""Configuration settings for the API."""

import logging
from functools import lru_cache

from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    """Configuration settings for the API."""

    environment: str = "dev"
    testing: bool = bool(0)
    database_url: str = "sqlite://data/db.sqlite3"


@lru_cache
def get_settings() -> BaseSettings:
    """Get the configuration settings."""
    log.info("Loading config settings from the environment...")
    return Settings()
