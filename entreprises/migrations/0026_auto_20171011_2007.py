# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-11 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entreprises', '0025_auto_20171011_1946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rapport_tuteur_entreprise',
            options={'ordering': ['-nom'], 'verbose_name_plural': '5. Evaluations'},
        ),
        migrations.AddField(
            model_name='rapport_tuteur_entreprise',
            name='commentaire',
            field=models.TextField(blank=True, null=True, verbose_name='Commentaire général sur la prestation en entreprise'),
        ),
    ]
