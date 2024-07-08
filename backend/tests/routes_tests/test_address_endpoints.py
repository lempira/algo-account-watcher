"""Tests for the address endpoints."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, AsyncGenerator, Generator

import pytest
from fastapi import status

from api.models.account import Account
from api.models.notification import Notification
from tests.conftest import seed_accounts

if TYPE_CHECKING:
    from _pytest.monkeypatch import MonkeyPatch
    from starlette.testclient import TestClient

mock_valid_account_info = {
    "address": "mock-address-valid",
    "amount": 123456,
}
mock_invalid_account_info = {
    "address": "mock-address-invalid",
}


class MockAlgodClient:
    """Mock AlgodClient class for testing."""

    def __init__(self, mock_algod_client_response: dict[str, Any]) -> None:
        """Initialize the MockAlgodClient class."""
        self.mock_algod_client_response = mock_algod_client_response
        self.account_info_called = 0

    def account_info(self, _: str) -> dict[str, Any]:
        """Mock account_info method."""
        self.account_info_called += 1
        return self.mock_algod_client_response


@pytest.fixture()
def mock_algod_client(
    monkeypatch: Generator[MonkeyPatch],
    mock_algod_client_response: dict[str, Any],
) -> MockAlgodClient:
    """Mock AlgodClient for testing."""
    mock_algod_client = MockAlgodClient(mock_algod_client_response)
    monkeypatch.setattr("api.utils.algod_client", mock_algod_client)
    return mock_algod_client


@pytest.mark.asyncio()
async def test_get_all_watched_addresses(test_app_with_db_and_data: AsyncGenerator[TestClient, None]) -> None:
    """Test case for the get_all_watched_addresses."""
    response = test_app_with_db_and_data.get("/addresses/all")

    assert response.status_code == status.HTTP_200_OK
    response_addresses = [a.get("address") for a in response.json()]
    assert len(response_addresses) == len(seed_accounts)


@pytest.mark.asyncio()
@pytest.mark.parametrize("mock_algod_client_response", [mock_valid_account_info])
async def test_add_address_success(
    test_app_with_db: Generator[TestClient, None],
    mock_algod_client: MockAlgodClient,
) -> None:
    """Test case for the add_address endpoint."""
    response = test_app_with_db.post("/addresses/add", data=json.dumps({"address": "test-address"}))

    assert response.status_code == status.HTTP_201_CREATED
    assert mock_algod_client.account_info_called == 1
    accounts = await Account.filter(address=mock_valid_account_info.get("address"))
    assert len(accounts) == 1


@pytest.mark.asyncio()
@pytest.mark.parametrize("mock_algod_client_response", [mock_invalid_account_info])
async def test_add_address_fail(
    test_app_with_db: Generator[TestClient, None],
    mock_algod_client: MockAlgodClient,
) -> None:
    """Test case for the add_address endpoint when it fails."""
    response = test_app_with_db.post("/addresses/add", data=json.dumps({"address": "test-address"}))

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert mock_algod_client.account_info_called == 1
    accounts = await Account.filter(address=mock_invalid_account_info.get("address"))
    assert len(accounts) == 0


@pytest.mark.asyncio()
async def test_delete_address(test_app_with_db_and_data: AsyncGenerator[TestClient, None]) -> None:
    """Test case for the removing a watched address."""
    first_seeded_address = seed_accounts[0].get("address")
    response = test_app_with_db_and_data.delete(
        f"/addresses/{first_seeded_address}",
    )

    assert response.status_code == status.HTTP_200_OK
    assert first_seeded_address not in [account.address for account in await Account.all()]
    # Assert notifications for the address are also deleted
    assert first_seeded_address not in [notification.address for notification in await Notification.all()]
