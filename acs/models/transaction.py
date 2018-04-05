from django.db import models

from acs.models import Profile


class Transaction(models.Model):
    student = models.ForeignKey(Profile, null=True)
    when = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(null=True)
