from tortoise import fields, models


class Notification(models.Model):
    address = fields.CharField(max_length=256, unique=True, pk=True)
    previous_amount = fields.BigIntField()
    current_amount = fields.BigIntField()
    message = fields.TextField()

    class Meta:
        table = "Notification"

    def __str__(self):
        return self.address
