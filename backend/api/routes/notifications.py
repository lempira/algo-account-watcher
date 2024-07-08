"""Routes for notifications on watched addresses."""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter
from pydantic import BaseModel

from api.models.notification import Notification, Notification_Pydantic

if TYPE_CHECKING:
    from tortoise.contrib.pydantic import PydanticModel

router = APIRouter()


### MODELS ###
class AddressInput(BaseModel):
    """Address input model."""

    address: str


### ROUTES ###
@router.get(
    "/all",
    response_model=list[Notification_Pydantic],
    status_code=200,
    description="Get all notifications for all addresses",
)
async def get_all_notifications() -> list[PydanticModel]:
    """Get all notification for all addresses."""
    return await Notification_Pydantic.from_queryset(Notification.all())


@router.get(
    "/{address}",
    response_model=list[Notification_Pydantic],
    status_code=200,
    description="Get all notifications for a specific address",
)
async def get_notifications_by_address(address: str) -> list[PydanticModel]:
    """Get all Algorand addresses being watched."""
    return await Notification_Pydantic.from_queryset(Notification.filter(address=address))
