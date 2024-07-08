"""Module containing test fixtures for the backend."""

from time import sleep
from typing import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from starlette.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise

from api.config import Settings, get_settings
from api.main import create_application
from api.models.account import Account


def get_settings_override() -> Settings:
    """Override the settings for testing.

    Returns
    -------
        Settings: The overridden settings.

    """
    return Settings(testing=1, environment="dev")


@pytest.fixture(scope="module")
def test_app_with_db() -> Generator[TestClient, None]:
    """Set up the test application with a database."""
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    register_tortoise(
        app,
        db_url="sqlite://:memory:",
        modules={"models": ["api.models.account", "api.models.notification"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    with TestClient(app) as test_client:
        yield test_client


@pytest_asyncio.fixture(scope="module")
async def test_app_with_db_and_data() -> AsyncGenerator[TestClient, None]:
    """Set up the test application with a database and data.

    Returns
    -------
    AsyncGenerator[TestClient, None]: The test client.

    """
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    register_tortoise(
        app,
        db_url="sqlite://:memory:",
        modules={"models": ["api.models.account", "api.models.notification"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

    with TestClient(app) as test_client:
        sleep(3)  # noqa: ASYNC251
        mock_addresses = ["mock-address-1", "mock-address-2"]
        await Account.create(address=mock_addresses[0], amount=123456)
        await Account.create(address=mock_addresses[1], amount=234567)

        yield test_client
