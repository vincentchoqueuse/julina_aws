# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-02 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entreprises', '0017_auto_20170902_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrat',
            name='intitule',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]