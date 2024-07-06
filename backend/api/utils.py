import logging
from typing import List
from algosdk.v2client import algod
from api.models.account import Account, Account_Pydantic
from pydantic import ValidationError


log = logging.getLogger("uvicorn")

ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"
ALGOD_TOKEN = ""
algod_client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)


def get_account_info(address: str) -> Account:
    log.info(f"Getting account info for {address}...")
    account_info = algod_client.account_info(address)
    try:
        account_model = Account_Pydantic(**account_info)
    except ValidationError as e:
        log.error("Validation error:", e.json())
        return None

    return account_model
