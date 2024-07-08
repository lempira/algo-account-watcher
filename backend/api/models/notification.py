"""Model for the Notification object."""

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Notification(models.Model):
    """Represents a notification for an account."""

    address = fields.CharField(max_length=256)
    previous_amount = fields.BigIntField()
    current_amount = fields.BigIntField()
    message = fields.TextField()
    created = fields.DatetimeField(auto_now_add=True)

    class Meta:
        """Metadata for the Notification model."""

        table = "Notification"

    def __str__(self) -> str:
        """Return the string representation of the notification."""
        return self.address

Notification_Pydantic = pydantic_model_creator(Notification, name="Notification")
