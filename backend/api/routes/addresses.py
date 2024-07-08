"""Routes for managing Algorand addresses being watched."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, ValidationError

from api.models.account import Account, Account_Pydantic
from api.utils import get_account_info

router = APIRouter()


### MODELS ###
class AddressInput(BaseModel):
    """Address input model."""

    address: str


class StatusResponse(BaseModel):
    """Status response model."""

    message: str


### ROUTES ###
@router.get(
    "/all",
    response_model=list[Account_Pydantic],
    status_code=200,
    description="Get all Algorand addresses being watched",
)
async def get_all_watched_addresses() -> list[Any]:
    """Get all Algorand addresses being watched."""
    return await Account_Pydantic.from_queryset(Account.all())


@router.post(
    "/add",
    response_model=Account_Pydantic,
    status_code=201,
    description="Add a new Algorand address to be watched.",
)
async def add_address(address: AddressInput) -> Any:  # noqa: ANN401
    """Add a new Algorand address to be watched."""
    try:
        account_info = get_account_info(address.address)
    except ValidationError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Account information failed validation: {e!s}",
        ) from e
    except Exception as e:  # noqa: BLE001
        raise HTTPException(
            status_code=404,
            detail=f"Error getting account info: {e!s}. It's possible that the address does not exist.",
        ) from None

    return await Account.create(**account_info.model_dump())


@router.delete("/delete", response_model=StatusResponse)
async def delete_address(address: AddressInput) -> StatusResponse:
    """Delete an Algorand address from the watched list."""
    deleted_count = await Account.filter(address=address.address).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Address {address.address} not found")
    return StatusResponse(message=f"Deleted address {address.address} from watched list")
