# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-10 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0020_auto_20171010_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='consigne_feuille_emargement',
            field=models.TextField(blank=True, null=True),
        ),
    ]
