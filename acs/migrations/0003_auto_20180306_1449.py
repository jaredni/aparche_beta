# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acs', '0002_auto_20180206_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mother_birthday',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mother_citizenship',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mother_contact',
            field=models.CharField(max_length=11, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mother_lname',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mother_mname',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mother_occupation',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mother_religion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
