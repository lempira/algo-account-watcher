"""Contains tasks related to account watching and notifications."""

from __future__ import annotations

import logging

from fastapi_utils.tasks import repeat_every

from api.models.account import Account
from api.models.notification import Notification
from api.routes.addresses import delete_address, get_all_watched_addresses
from api.utils import get_account_info

log = logging.getLogger("uvicorn")


async def generate_notifications(current_local_accounts: list[Account], algo_node_accounts: list[Account]) -> None:
    """Generate notifications based on the comparison of local and Algorand node accounts.

    Args:
    ----
        current_local_accounts (List[Account]): List of current local accounts.
        algo_node_accounts (List[Account]): List of Algorand node accounts.

    Returns:
    -------
        None

    """
    algo_node_accounts_map = {account.address: account for account in algo_node_accounts}
    for local_account in current_local_accounts:
        algo_node_account = algo_node_accounts_map.get(local_account.address)
        if not algo_node_account:
            log.warning(
                f"Account {local_account.address} not found in Algorand Nodes. Removing account from watched list.",
            )
            delete_address({"address": local_account.address})
            continue

        if local_account.amount != algo_node_account.amount:
            log.info(
                f"""Account {local_account.address} balance changed from {local_account.amount}
                to {algo_node_account.amount}""",
            )
            try:
                await Notification.create(
                    address=local_account.address,
                    previous_amount=local_account.amount,
                    current_amount=algo_node_account.amount,
                    message="Amount Updated",
                )
            except Exception:
                log.exception("Error creating notification")
            log.debug(
                f"""Updating Account {local_account.address} balance from
                {local_account.amount} to {algo_node_account.amount}""",
            )
            log.info(algo_node_account.model_dump())
            try:
                await Account.filter(address=local_account.address).update(amount=algo_node_account.amount)
            except Exception:
                log.exception("Error updating account")

        else:
            log.debug(
                f"""Account {local_account.address} balance unchanged at
                {local_account.amount}""",
            )


@repeat_every(seconds=60)
async def check_watched_accounts_state() -> None:
    """Check the state of watched accounts and generate notifications."""
    log.info("Checking the state of watched accounts...")
    current_local_accounts = await get_all_watched_addresses()
    algo_node_accounts = [get_account_info(account.address) for account in current_local_accounts]
    await generate_notifications(current_local_accounts, algo_node_accounts)
