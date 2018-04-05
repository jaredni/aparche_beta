# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acs', '0004_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='tuition',
        ),
        migrations.AlterField(
            model_name='profile',
            name='year_level',
            field=models.ForeignKey(related_name='level', to='acs.Level', null=True),
        ),
    ]
