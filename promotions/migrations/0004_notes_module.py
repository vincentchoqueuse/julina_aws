# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0002_auto_20170724_2149'),
        ('promotions', '0003_auto_20170725_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='formations.Module'),
            preserve_default=False,
        ),
    ]
