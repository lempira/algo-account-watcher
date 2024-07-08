"""Provides utility functions for the API."""

import logging

from algosdk.v2client import algod
from pydantic import ValidationError

from api.models.account import Account, Account_Pydantic

log = logging.getLogger("uvicorn")

ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"
ALGOD_TOKEN = ""
algod_client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)


def get_account_info(address: str) -> Account:
    """Get account information for the given address.

    Args:
    ----
        address (str): The address of the account.

    Returns:
    -------
        Account: The account information.

    Raises:
    ------
        ValidationError: If there is a validation error.

    """
    log.info(f"Getting account info for {address}...")
    account_info = algod_client.account_info(address)
    try:
        account_model = Account_Pydantic(**account_info)
    except ValidationError as e:
        log.exception(f"Validation error: {e.json()}")
        raise

    return account_model
