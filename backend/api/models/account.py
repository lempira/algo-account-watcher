from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import ConfigDict


class Account(models.Model):
    address = fields.CharField(max_length=256, unique=True, pk=True)
    amount = fields.BigIntField()

    class Meta:
        table = "Account"

    class PydanticMeta:
        model_config = ConfigDict(extra="ignore")

    def __str__(self):
        return self.address


Account_Pydantic = pydantic_model_creator(Account, name="Account")
