# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-24 07:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0006_auto_20170820_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enseignant',
            name='formation',
        ),
    ]