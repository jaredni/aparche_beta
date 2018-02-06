from django.db import models

GENDER_CHOICES = (
    (0, 'Female'),
    (1, 'Male'),
)

YEAR_LEVEL_CHOICES = (
    (0, 'Nursery'),             # 3 years old by june
    (1, 'Pre-K'),               # 4 years old by june
    (2, 'Kindergarten'),         # 5 years old by june
    (3, 'Grade 1'),
    (4, 'Grade 2'),
    (5, 'Grade 3'),
    (6, 'Grade 4'),
    (7, 'Grade 5'),
    (8, 'Grade 6'),
)


class Profile(models.Model):
    # learner's information
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    middle_name = models.CharField(max_length=200, null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True)
    year_level = models.IntegerField(choices=YEAR_LEVEL_CHOICES, null=True)
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
    father_lname = models.CharField(max_length=200, blank=True, null=True)
    father_mname = models.CharField(max_length=200, blank=True, null=True)
    father_citizenship = models.CharField(
        max_length=200, blank=True, null=True)
    father_religion = models.CharField(max_length=200, blank=True, null=True)
    father_contact = models.CharField(max_length=11, blank=True, null=True)
    father_occupation = models.CharField(max_length=200, blank=True, null=True)
    father_birthday = models.DateField(blank=True, null=True)

    tuition = models.DecimalField(max_digits=2, decimal_places=2, null=True)
# Create your models here.
