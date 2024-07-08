"""Model for the Algorand Account object."""

from pydantic import ConfigDict
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Account(models.Model):
    """Represents an Algorand account."""

    address = fields.CharField(max_length=256, unique=True, primary_key=True)
    amount = fields.BigIntField()

    class Meta:
        """Metadata for the Account model."""

        table = "Account"

    class PydanticMeta:
        """Pydantic metadata for the Account model.

        This is used to ignore the extra field in the Pydantic model.
        """

        model_config = ConfigDict(extra="ignore")

    def __str__(self) -> str:
        """Return the string representation of the account."""
        return self.address


Account_Pydantic = pydantic_model_creator(Account, name="Account")
