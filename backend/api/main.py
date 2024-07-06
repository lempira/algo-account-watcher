import logging
from fastapi import FastAPI, Depends
from api.config import get_settings, Settings
from api.routes import addresses
from api.tasks import check_watched_accounts_state
from contextlib import asynccontextmanager
from api.db import init_db
from tortoise.contrib.fastapi import RegisterTortoise
from tortoise.contrib.fastapi import register_tortoise
from api.config import get_settings


log = logging.getLogger("uvicorn")
settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("Creating a new application lifecycle context...")
    await check_watched_accounts_state()

    yield
    log.info("Destroying the application lifecycle context...")


def create_application() -> FastAPI:
    application = FastAPI(lifespan=lifespan)
    application.include_router(
        addresses.router, prefix="/addresses", tags=["addresses"]
    )

    return application


app = create_application()

# init_db(app)
register_tortoise(
    app,
    db_url=settings.database_url,
    modules={"models": ["api.models.account", "api.models.notification"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
