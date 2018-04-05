# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acs', '0003_auto_20180306_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher', models.CharField(max_length=200, null=True)),
                ('year_level', models.CharField(max_length=200, unique=True, null=True)),
                ('tuition', models.IntegerField(null=True)),
                ('max_students', models.IntegerField(default=20)),
            ],
        ),
    ]
