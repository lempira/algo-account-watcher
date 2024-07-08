"""Tests for the notification endpoints."""

from typing import AsyncGenerator

import pytest
from fastapi import status
from starlette.testclient import TestClient

from tests.conftest import seed_notifications


@pytest.mark.asyncio()
async def test_get_all_notifications(test_app_with_db_and_data: AsyncGenerator[TestClient, None]) -> None:
    """Test case for the getting all the notifications."""
    response = test_app_with_db_and_data.get("/notifications/all")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == len(seed_notifications)


@pytest.mark.asyncio()
async def test_get_all_notifications_by_address(test_app_with_db_and_data: AsyncGenerator[TestClient, None]) -> None:
    """Test case for getting all the notifications for a particular address."""
    seeded_address = seed_notifications[0].get("address")
    filtered_notifications = [n for n in seed_notifications if n.get("address") == seeded_address]
    response = test_app_with_db_and_data.get(f"/notifications/{seeded_address}")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == len(filtered_notifications)
