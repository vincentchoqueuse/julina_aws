# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0004_auto_20170725_1408'),
        ('promotions', '0012_auto_20170726_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupe',
            name='parcours',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formations.Parcours'),
        ),
    ]
