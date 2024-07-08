"""Main module of the API."""

import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from api.config import get_settings
from api.routes import addresses
from api.tasks import check_watched_accounts_state

log = logging.getLogger("uvicorn")
settings = get_settings()

origins = [
    "*",  # Allow all origins. Be cautious when using this in production.
]


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:  # noqa: ARG001
    """Context manager for the application lifecycle."""
    log.info("Creating a new application lifecycle context...")
    await check_watched_accounts_state()

    yield
    log.info("Destroying the application lifecycle context...")


def create_application() -> FastAPI:
    """Create the FastAPI application."""
    application = FastAPI(lifespan=lifespan)
    application.include_router(addresses.router, prefix="/addresses", tags=["addresses"])

    return application


app = create_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(
    app,
    db_url=settings.database_url,
    modules={"models": ["api.models.account", "api.models.notification"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
