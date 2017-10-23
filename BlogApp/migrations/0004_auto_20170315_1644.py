# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0003_auto_20170315_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('author', models.CharField(max_length=16, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('content', models.TextField(verbose_name=b'\xe5\x8d\x9a\xe5\xae\xa2\xe6\xad\xa3\xe6\x96\x87')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name=b'\xe7\xa7\xb0\xe5\x91\xbc')),
                ('email', models.EmailField(max_length=75, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('content', models.CharField(max_length=240, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('blog', models.ForeignKey(verbose_name=b'\xe5\x8d\x9a\xe5\xae\xa2', to='BlogApp.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blog',
            name='catagory',
            field=models.ForeignKey(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', to='BlogApp.Catagory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='BlogApp.Tag', verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe'),
            preserve_default=True,
        ),
    ]
