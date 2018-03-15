# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-27 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0018_auto_20170824_0701'),
        ('projets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projet_tuteure',
            name='etudiant',
        ),
        migrations.AddField(
            model_name='projet_tuteure',
            name='affectation',
            field=models.ManyToManyField(blank=True, null=True, to='promotions.Affectation_Etudiant'),
        ),
    ]
