from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


class Operation(models.Model):
    OPERATIONS_CHOICES = (
      (1, _('Addition')),
      (2, _('Subtraction')),
      (3, _('Multiplication')),
      (4, _('Division')),
      (5, _('Square root')),
      (6, _('Random string')),
    )

    type = models.PositiveSmallIntegerField(choices=OPERATIONS_CHOICES)
    cost = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.get_type_display()


class Record(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()
    user_balance = models.PositiveSmallIntegerField()
    operation_response = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)

    @property
    def friendly_date(self):
        return self.date.date()

    def __str__(self):
        return f"{self.operation} - {self.user} - {self.date.date()}"
