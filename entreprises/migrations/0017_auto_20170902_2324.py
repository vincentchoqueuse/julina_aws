# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-02 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entreprises', '0016_entreprise_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entreprise',
            name='siret',
            field=models.BigIntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]