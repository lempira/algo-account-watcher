import os
import logging
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from api.config import get_settings
from tortoise.contrib.fastapi import RegisterTortoise
from typing import AsyncGenerator

log = logging.getLogger("uvicorn")
settings = get_settings()


TORTOISE_ORM = {
    "connections": {"default": settings.database_url},
    "apps": {
        "models": {
            "models": [
                "api.models.account",
                "api.models.notification",
                "aerich.models",
            ],
            "default_connection": "default",
        },
    },
}


async def init_db(app: FastAPI) -> AsyncGenerator[None, None]:
    log.info("Initializing the database connection...")
    register_tortoise(
        app,
        db_url=settings.database_url,
        modules={"models": ["api.models.account", "api.models.notification"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )
