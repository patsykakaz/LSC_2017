# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-03 13:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0005_auto_20160729_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='campagne',
            name='clientKey',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='MAIN.Client'),
            preserve_default=False,
        ),
    ]
