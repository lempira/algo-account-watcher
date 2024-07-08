"""Module containing test fixtures for the backend."""

import asyncio
import os
from time import sleep
from typing import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from starlette.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise

from api.config import Settings, get_settings
from api.main import create_application
from api.models.account import Account
from api.models.notification import Notification

seed_accounts = [
    {"address": "mock-address-1", "amount": 123456},
    {"address": "mock-address-2", "amount": 234567},
]
seed_notifications = [
    {"address": "mock-address-1", "previous_amount": 123456, "current_amount": 234567, "message": "Amount updated"},
    {"address": "mock-address-1", "previous_amount": 234567, "current_amount": 234569, "message": "Amount updated"},
    {"address": "mock-address-2", "previous_amount": 123256, "current_amount": 234565, "message": "Amount updated"},
    {"address": "mock-address-2", "previous_amount": 234565, "current_amount": 224565, "message": "Amount updated"},
]


def get_settings_override() -> Settings:
    """Override the settings for testing.

    Returns
    -------
        Settings: The overridden settings.

    """
    return Settings(testing=1, environment="dev")


@pytest.fixture()
def test_app_with_db() -> Generator[TestClient, None, None]:
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


@pytest_asyncio.fixture(scope="function")
async def test_app_with_db_and_data() -> AsyncGenerator[TestClient, None]:
    """Set up the test application with a database and data.

    Returns
    -------
    AsyncGenerator[TestClient, None]: The test client.

    """
    os.environ["DATABASE_URL"] = "sqlite://:memory:"
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
        # Clear DB
        await Account.all().delete()
        await Notification.all().delete()

        # Seed DB
        await asyncio.gather(
            *[
                Account.create(address=account.get("address"), amount=account.get("amount"))
                for account in seed_accounts
            ],
        )
        await asyncio.gather(
            *[
                Notification.create(
                    address=notification.get("address"),
                    previous_amount=notification.get("previous_amount"),
                    current_amount=notification.get("current_amount"),
                    message=notification.get("message"),
                )
                for notification in seed_notifications
            ],
        )

        yield test_client
