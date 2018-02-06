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
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    year_level = models.IntegerField(choices=YEAR_LEVEL_CHOICES)
    citizenship = models.CharField(max_length=200)
    religion = models.CharField(max_length=200)
    residence_tel_no = models.CharField(max_length=11)
    birthday = models.DateField()

    # location of birth
    birth_city = models.CharField(max_length=200)
    birth_municipality = models.CharField(max_length=200)
    birth_barangay = models.CharField(max_length=200)
    birth_street = models.CharField(max_length=200)

    # present address
    address_city = models.CharField(max_length=200)
    address_municipality = models.CharField(max_length=200)
    address_barangay = models.CharField(max_length=200)
    address_street = models.CharField(max_length=200)

    # father's information
    father_fname = models.CharField(max_length=200)
    father_lname = models.CharField(max_length=200)
    father_mname = models.CharField(max_length=200)
    father_citizenship = models.CharField(max_length=200)
    father_religion = models.CharField(max_length=200)
    father_contact = models.CharField(max_length=11)
    father_occupation = models.CharField(max_length=200)
    father_birthday = models.DateField()

    # mother's information
    mother_fname = models.CharField(max_length=200)
    father_lname = models.CharField(max_length=200)
    father_mname = models.CharField(max_length=200)
    father_citizenship = models.CharField(max_length=200)
    father_religion = models.CharField(max_length=200)
    father_contact = models.CharField(max_length=11)
    father_occupation = models.CharField(max_length=200)
    father_birthday = models.DateField()

    tuition = models.DecimalField(max_digits=2, decimal_places=2)
# Create your models here.
