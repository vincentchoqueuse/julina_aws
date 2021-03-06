# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entreprises', '0003_auto_20170725_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='CQPM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('description', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='contrat',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='responsable_administratif',
            name='poste',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tuteur_entreprise',
            name='poste',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='contrat',
            name='num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrat',
            name='cqpm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entreprises.CQPM'),
        ),
    ]
