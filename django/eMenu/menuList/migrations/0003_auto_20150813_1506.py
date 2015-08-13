# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuList', '0002_remove_menu_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='meals',
            field=models.ManyToManyField(to='menuList.Meal', blank=True),
        ),
    ]
