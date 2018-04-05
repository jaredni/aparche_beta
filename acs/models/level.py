from django.db import models


class Level(models.Model):
    teacher = models.CharField(max_length=200, null=True)
    year_level = models.CharField(unique=True, max_length=200, null=True)
    tuition = models.IntegerField(null=True)
    max_students = models.IntegerField(default=20)
