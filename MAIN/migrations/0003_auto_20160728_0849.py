# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-28 08:49
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0002_auto_20160728_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='illustration',
            field=mezzanine.core.fields.FileField(default=False, max_length=255, null=True, verbose_name='Illustration'),
        ),
    ]
