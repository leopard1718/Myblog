# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_auto_20170315_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='blogs_home',
            name='catagory',
        ),
        migrations.DeleteModel(
            name='Blogs_catagory',
        ),
        migrations.RemoveField(
            model_name='blogs_home',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Blogs_tag',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Blogs_home',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
