# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entreprises', '0002_auto_20170724_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entreprise',
            name='apet700',
        ),
        migrations.RemoveField(
            model_name='entreprise',
            name='l1_normalisee',
        ),
        migrations.RemoveField(
            model_name='entreprise',
            name='l4_normalisee',
        ),
        migrations.RemoveField(
            model_name='entreprise',
            name='l6_normalisee',
        ),
        migrations.RemoveField(
            model_name='entreprise',
            name='l7_normalisee',
        ),
        migrations.RemoveField(
            model_name='entreprise',
            name='libapen',
        ),
        migrations.RemoveField(
            model_name='entreprise',
            name='nomen_long',
        ),
        migrations.AddField(
            model_name='entreprise',
            name='activite',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='entreprise',
            name='adresse_rue',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entreprise',
            name='adresse_ville',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='entreprise',
            name='adresse_zip',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entreprise',
            name='naf',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entreprise',
            name='nom',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entreprise',
            name='statut',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]