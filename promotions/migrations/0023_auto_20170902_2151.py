# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-02 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0022_delete_etudiant2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='code_nip',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='etudid',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
