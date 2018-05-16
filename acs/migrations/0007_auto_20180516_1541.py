# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acs', '0006_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='student',
            field=models.ForeignKey(related_name='transaction', to='acs.Profile', null=True),
        ),
    ]
