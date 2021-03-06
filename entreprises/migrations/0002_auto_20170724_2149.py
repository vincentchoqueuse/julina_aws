# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entreprises', '0001_initial'),
        ('formations', '0001_initial'),
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrat',
            name='etudiant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='promotions.Etudiant'),
        ),
        migrations.AddField(
            model_name='contrat',
            name='promotion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='promotions.Promotion'),
        ),
        migrations.AddField(
            model_name='contrat',
            name='responsable_administratif',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entreprises.Responsable_Administratif'),
        ),
        migrations.AddField(
            model_name='contrat',
            name='tuteur_entreprise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entreprises.Tuteur_Entreprise'),
        ),
        migrations.AddField(
            model_name='contrat',
            name='tuteur_formation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formations.Enseignant'),
        ),
    ]
