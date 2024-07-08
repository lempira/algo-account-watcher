"""Tests for the utils module."""

from typing import Generator

import pytest
from _pytest.monkeypatch import MonkeyPatch
from pydantic import ValidationError

from api.utils import algod_client, get_account_info

valid_address = "some_valid_address"
valid_account_info = {
    "address": valid_address,
    "amount": 123456,
}
invalid_account_info = {
    "address": valid_address,
    # missing amount which is required
}


class MockLogger:
    """Mock logger class for testing."""

    def __init__(self) -> None:
        """Initialize the MockLogger class."""
        self.info_messages = []
        self.error_messages = []

    def info(self, log_message: str) -> None:
        """Logs an info message."""  # noqa: D401
        self.info_messages.append(log_message)

    def error(self, log_message: str) -> None:
        """Logs an error message."""  # noqa: D401
        self.error_messages.append(log_message)

    def exception(self, log_message: str) -> None:
        """Logs an exception."""  # noqa: D401
        self.error_messages.append(log_message)


@pytest.fixture()
def mock_logger(monkeypatch: Generator[MonkeyPatch, None, None]) -> MockLogger:
    """Mock logger fixture for testing."""
    logger = MockLogger()
    monkeypatch.setattr("api.utils.log", logger)
    return logger


def test_get_account_info_success(mocker: Generator[None, None, None]) -> None:
    """Test case for the get_account_info function when it succeeds."""
    mocker.patch.object(algod_client, "account_info", return_value=valid_account_info)

    account = get_account_info(valid_address)

    assert account.address == valid_account_info.get("address")
    assert account.amount == valid_account_info.get("amount")

    algod_client.account_info.assert_called_once_with(valid_address)


def test_get_account_info_fail(mock_logger: MockLogger, mocker: Generator[None, None, None]) -> None:
    """Test case for the get_account_info function when it fails."""
    mocker.patch.object(algod_client, "account_info", return_value=invalid_account_info)

    with pytest.raises(ValidationError):
        get_account_info(valid_address)

    assert len(mock_logger.error_messages) > 0
