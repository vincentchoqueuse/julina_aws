# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-23 11:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0033_auto_20170919_1920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='etudiant',
            options={'ordering': ['nom']},
        ),
    ]
