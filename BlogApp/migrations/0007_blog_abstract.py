# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0006_auto_20170315_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='abstract',
            field=models.CharField(help_text=b'\xe5\x8f\xaf\xe9\x80\x89\xef\xbc\x8c\xe5\xa6\x82\xe8\x8b\xa5\xe4\xb8\xba\xe7\xa9\xba\xe5\x88\x99\xe6\x91\x98\xe5\x8f\x96\xe6\xad\xa3\xe6\x96\x87\xe5\x89\x8d54\xe4\xb8\xaa\xe5\xad\x97\xe7\xac\xa6', max_length=54, null=True, verbose_name=b'\xe6\x91\x98\xe8\xa6\x81', blank=True),
            preserve_default=True,
        ),
    ]
