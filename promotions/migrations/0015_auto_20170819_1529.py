# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-19 15:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0014_remove_groupe_parcours'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='affectation_etudiant',
            options={'ordering': ['etudiant__nom'], 'verbose_name_plural': '4. Affectation Etudiant'},
        ),
    ]