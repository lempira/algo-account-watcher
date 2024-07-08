"""Main module of the API."""

import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import RegisterTortoise

from api.config import get_settings
from api.routes import addresses, notifications
from api.tasks import check_watched_accounts_state

log = logging.getLogger("uvicorn")
settings = get_settings()
temp=1
origins = settings.allowable_origins


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    """Context manager for the application lifecycle."""
    log.info("Creating a new application lifecycle context...")
    await check_watched_accounts_state()
    async with RegisterTortoise(
        app,
        db_url=settings.database_url,
        modules={"models": ["api.models.account", "api.models.notification"]},
        generate_schemas=True,
        add_exception_handlers=True,
    ):
        yield

    log.info("Destroying the application lifecycle context...")


def create_application() -> FastAPI:
    """Create the FastAPI application."""
    application = FastAPI(lifespan=lifespan, swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})
    application.include_router(addresses.router, prefix="/addresses", tags=["addresses"])
    application.include_router(notifications.router, prefix="/notifications", tags=["notifications"])

    return application


app = create_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
)
