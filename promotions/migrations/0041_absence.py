# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-12 19:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import promotions.models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0021_formation_consigne_feuille_emargement'),
        ('promotions', '0040_auto_20171006_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('debut', models.DateField(blank=True, default=datetime.datetime.now)),
                ('fin', models.DateField(blank=True, default=datetime.datetime.now)),
                ('commentaire_raf', models.TextField(blank=True, max_length=400, null=True)),
                ('commentaire_adm', models.TextField(blank=True, max_length=400, null=True)),
                ('commentaire_ens', models.TextField(blank=True, max_length=400, null=True)),
                ('justification', models.FileField(upload_to=promotions.models.get_justification_path)),
                ('statut', models.CharField(choices=[('NJ', 'Non Justifié'), ('EC', 'En Cours'), ('J', 'Justifié')], default='NJ', max_length=10)),
                ('affectation_etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promotions.Affectation_Etudiant')),
                ('enseignants', models.ManyToManyField(to='formations.Enseignant')),
            ],
        ),
    ]
