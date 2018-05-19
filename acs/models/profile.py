from django.db import models
from django.db.models import Sum

from acs.models.level import Level

GENDER_CHOICES = (
    (0, 'Female'),
    (1, 'Male'),
)


class Profile(models.Model):
    # learner's information
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    middle_name = models.CharField(max_length=200, null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True)
    year_level = models.ForeignKey(Level, related_name='level', null=True)
    citizenship = models.CharField(max_length=200, blank=True, null=True)
    religion = models.CharField(max_length=200, blank=True, null=True)
    residence_tel_no = models.CharField(max_length=11, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    # location of birth
    birth_city = models.CharField(max_length=200, blank=True, null=True)
    birth_municipality = models.CharField(
        max_length=200, blank=True, null=True)
    birth_barangay = models.CharField(max_length=200, blank=True, null=True)
    birth_street = models.CharField(max_length=200, blank=True, null=True)

    # present address
    address_city = models.CharField(max_length=200, blank=True, null=True)
    address_municipality = models.CharField(
        max_length=200, blank=True, null=True)
    address_barangay = models.CharField(max_length=200, blank=True, null=True)
    address_street = models.CharField(max_length=200, blank=True, null=True)

    # father's information
    father_fname = models.CharField(max_length=200, blank=True, null=True)
    father_lname = models.CharField(max_length=200, blank=True, null=True)
    father_mname = models.CharField(max_length=200, blank=True, null=True)
    father_citizenship = models.CharField(
        max_length=200, blank=True, null=True)
    father_religion = models.CharField(max_length=200, blank=True, null=True)
    father_contact = models.CharField(max_length=11, blank=True, null=True)
    father_occupation = models.CharField(max_length=200, blank=True, null=True)
    father_birthday = models.DateField(blank=True, null=True)

    # mother's information
    mother_fname = models.CharField(max_length=200, blank=True, null=True)
    mother_lname = models.CharField(max_length=200, blank=True, null=True)
    mother_mname = models.CharField(max_length=200, blank=True, null=True)
    mother_citizenship = models.CharField(
        max_length=200, blank=True, null=True)
    mother_religion = models.CharField(max_length=200, blank=True, null=True)
    mother_contact = models.CharField(max_length=11, blank=True, null=True)
    mother_occupation = models.CharField(max_length=200, blank=True, null=True)
    mother_birthday = models.DateField(blank=True, null=True)
# Create your models here.

    def __str__(self):
        return '{} {}, {}'.format(
            self.last_name, self.first_name, self.middle_name)

    @property
    def get_total_paid(self):
        total_paid = self.transaction.aggregate(Sum('amount'))
        return total_paid['amount__sum']
