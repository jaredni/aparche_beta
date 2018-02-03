from django.db import models

class Profile(models.Model):
	first_name = models.CharField(max_length=200)
# Create your models here.
