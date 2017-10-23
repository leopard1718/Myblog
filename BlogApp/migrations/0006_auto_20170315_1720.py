# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0005_auto_20170315_1649'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogsPost',
        ),
        migrations.AlterField(
            model_name='catagory',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=16, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0'),
            preserve_default=True,
        ),
    ]
