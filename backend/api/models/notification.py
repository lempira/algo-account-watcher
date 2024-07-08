"""Models for the Notification object."""

from tortoise import fields, models


class Notification(models.Model):
    """Represents a notification for an account."""

    address = fields.CharField(max_length=256)
    previous_amount = fields.BigIntField()
    current_amount = fields.BigIntField()
    message = fields.TextField()

    class Meta:
        """Metadata for the Notification model."""

        table = "Notification"

    def __str__(self) -> str:
        """Return the string representation of the notification."""
        return self.address
