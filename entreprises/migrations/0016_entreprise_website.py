# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-26 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entreprises', '0015_remove_entreprise_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='entreprise',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
