# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 17:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('entreprises', '0010_auto_20170726_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapport_tuteur_formation',
            name='date_visite',
            field=models.DateField(default=datetime.datetime(2017, 7, 26, 17, 6, 56, 430847, tzinfo=utc), help_text='format: année-mois-jours (exemple 2014-03-1)'),
        ),
    ]
