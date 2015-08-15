# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuList', '0004_error'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='price',
            field=models.FloatField(default=10.0),
            preserve_default=False,
        ),
    ]
