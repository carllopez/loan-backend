from django.contrib.auth.models import User
from django.db import models


class UserBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    balance = models.PositiveIntegerField(default=500)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - balance"
