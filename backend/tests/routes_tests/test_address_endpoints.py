"""Tests for the address endpoints."""

from __future__ import annotations

import json
from typing import Any, Generator

import pytest
from _pytest.monkeypatch import MonkeyPatch  # noqa: TCH002
from starlette.testclient import TestClient  # noqa: TCH002

from api.models.account import Account

mock_valid_account_info = {
    "address": "mock-address-valid",
    "amount": 123456,
}
mock_invalid_account_info = {
    "address": "mock-address-invalid",
}

HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_404_NOT_FOUND = 404


class MockAlgodClient:
    """Mock AlgodClient class for testing."""

    def __init__(self, mock_algod_client_response: dict[str, Any]) -> None:
        """Initialize the MockAlgodClient class."""
        self.mock_algod_client_response = mock_algod_client_response
        self.account_info_called = 0

    def account_info(self) -> dict[str, Any]:
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
async def test_get_all_watched_addresses(test_app_with_db_and_data: Generator[TestClient, None]) -> None:
    """Test case for the get_all_watched_addresses."""
    response = test_app_with_db_and_data.get("/addresses/all")

    assert response.status_code == HTTP_200_OK
    response_addresses = [a.get("address") for a in response.json()]
    assert len(response_addresses) == 2  # noqa: PLR2004


@pytest.mark.asyncio()
@pytest.mark.parametrize("mock_algod_client_response", [mock_valid_account_info])
async def test_add_address_success(
    test_app_with_db: Generator[TestClient, None],
    mock_algod_client: MockAlgodClient,
) -> None:
    """Test case for the add_address endpoint."""
    response = test_app_with_db.post("/addresses/add", data=json.dumps({"address": "test-address"}))

    assert response.status_code == HTTP_201_CREATED
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

    assert response.status_code == HTTP_404_NOT_FOUND
    assert mock_algod_client.account_info_called == 1
    accounts = await Account.filter(address=mock_invalid_account_info.get("address"))
    assert len(accounts) == 0
