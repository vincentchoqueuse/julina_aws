# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0009_auto_20170725_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletin',
            name='moyenne',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]