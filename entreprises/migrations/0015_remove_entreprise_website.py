# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-26 12:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entreprises', '0014_auto_20170826_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entreprise',
            name='website',
        ),
    ]