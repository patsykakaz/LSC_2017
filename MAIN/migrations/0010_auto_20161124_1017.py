# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-24 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0009_fakeblog_fakebloggalery'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='linkedin',
            field=models.URLField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='worker',
            name='twitter',
            field=models.URLField(default=False, null=True),
        ),
    ]
