# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0007_blog_abstract'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catagory',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='catagory',
            new_name='category',
        ),
    ]
