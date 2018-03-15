# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-24 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0017_auto_20170821_0719'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='etudiant',
            options={'ordering': ['nom'], 'verbose_name_plural': '2. Etudiants'},
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='sexe',
            field=models.CharField(blank=True, choices=[('F', 'Feminin'), ('M', 'Masculin')], default='M', max_length=10, null=True),
        ),
    ]
