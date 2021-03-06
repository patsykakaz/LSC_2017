# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campagne',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('illustration', mezzanine.core.fields.FileField(max_length=255, verbose_name='Image')),
                ('baseline', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='CampagneCaptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', mezzanine.core.fields.FileField(max_length=255, verbose_name='Image')),
                ('description', models.TextField(blank=True, null=True)),
                ('Campagne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MAIN.Campagne')),
            ],
            options={
                'verbose_name': 'Captions',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('logo', mezzanine.core.fields.FileField(max_length=255, verbose_name='Logo')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
    ]
