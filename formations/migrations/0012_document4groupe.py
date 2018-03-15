# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-18 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import formations.models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0032_auto_20170918_2123'),
        ('formations', '0011_remove_devoir_etudiant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document4Groupe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=1)),
                ('nom', models.CharField(max_length=400)),
                ('file', models.FileField(upload_to=formations.models.get_document_path)),
                ('modification', models.DateTimeField(auto_now=True)),
                ('affectation_enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promotions.Affectation_Enseignant')),
            ],
        ),
    ]
