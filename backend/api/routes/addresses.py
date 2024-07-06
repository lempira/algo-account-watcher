from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api.models.account import Account, Account_Pydantic
from api.utils import get_account_info


router = APIRouter()


### MODELS ###
class AddressInput(BaseModel):
    address: str


class StatusResponse(BaseModel):
    message: str


### ROUTES ###
@router.get(
    "/all",
    response_model=List[Account_Pydantic],
    status_code=200,
    description="Get all Algorand addresses being watched",
)
async def get_all_watched_addresses():
    addresses = await Account_Pydantic.from_queryset(Account.all())
    return addresses


@router.post(
    "/add",
    response_model=Account_Pydantic,
    status_code=201,
    description="Add a new Algorand address to be watched.",
)
async def add_address(address: AddressInput):
    account_info = get_account_info(address.address)
    account = await Account.create(**account_info.model_dump())
    return account


@router.delete("/delete", response_model=StatusResponse)
async def delete_address(address: AddressInput):
    deleted_count = await Account.filter(address=address.address).delete()
    if not deleted_count:
        raise HTTPException(
            status_code=404, detail=f"Address {address.address} not found"
        )
    return StatusResponse(
        message=f"Deleted address {address.address} from watched list"
    )
