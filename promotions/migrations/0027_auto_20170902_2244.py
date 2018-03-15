# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-02 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0026_auto_20170902_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='affectation_etudiant',
            name='etudiant2',
        ),
        migrations.AlterField(
            model_name='promotion',
            name='etudiants',
            field=models.ManyToManyField(through='promotions.Affectation_Etudiant', to='promotions.Etudiant'),
        ),
        migrations.DeleteModel(
            name='Etudiant2',
        ),
    ]
