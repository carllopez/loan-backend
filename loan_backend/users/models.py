from django.contrib.auth.models import User
from django.db import models


class UserBalance(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	balance = models.PositiveIntegerField()
