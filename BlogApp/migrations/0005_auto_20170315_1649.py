# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0004_auto_20170315_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='name',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=16),
            preserve_default=True,
        ),
    ]
