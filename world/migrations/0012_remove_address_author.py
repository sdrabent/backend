# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0011_auto_20150906_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='author',
        ),
    ]
