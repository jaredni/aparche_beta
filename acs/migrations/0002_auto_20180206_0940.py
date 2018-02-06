# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address_barangay',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='address_city',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='address_municipality',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='address_street',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_barangay',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_city',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_municipality',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_street',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='citizenship',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='father_birthday',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='father_citizenship',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='father_contact',
            field=models.CharField(max_length=11, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='father_fname',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='father_lname',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='father_mname',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='father_occupation',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='father_religion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.IntegerField(null=True, choices=[(0, b'Female'), (1, b'Male')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mother_fname',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='religion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='residence_tel_no',
            field=models.CharField(max_length=11, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='tuition',
            field=models.DecimalField(null=True, max_digits=2, decimal_places=2),
        ),
        migrations.AddField(
            model_name='profile',
            name='year_level',
            field=models.IntegerField(null=True, choices=[(0, b'Nursery'), (1, b'Pre-K'), (2, b'Kindergarten'), (3, b'Grade 1'), (4, b'Grade 2'), (5, b'Grade 3'), (6, b'Grade 4'), (7, b'Grade 5'), (8, b'Grade 6')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
