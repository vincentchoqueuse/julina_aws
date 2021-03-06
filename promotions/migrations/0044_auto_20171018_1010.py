# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-18 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0043_auto_20171012_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='etudiant',
            options={'ordering': ['nom'], 'verbose_name_plural': '1. Etudiants'},
        ),
        migrations.AddField(
            model_name='affectation_etudiant',
            name='bulletin_visible',
            field=models.BooleanField(default=False, verbose_name='Communication du bulletin au tuteur entreprise'),
        ),
    ]
