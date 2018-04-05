# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acs', '0005_auto_20180405_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField(null=True)),
                ('student', models.ForeignKey(to='acs.Profile', null=True)),
            ],
        ),
    ]
