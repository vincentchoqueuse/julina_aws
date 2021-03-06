# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-02 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0018_auto_20170824_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupe',
            name='affectations',
            field=models.ManyToManyField(to='promotions.Affectation_Etudiant'),
        ),
        migrations.AlterField(
            model_name='affectation_enseignant',
            name='enseignant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='affectation_enseignant_set', to='formations.Enseignant'),
        ),
        migrations.AlterField(
            model_name='affectation_etudiant',
            name='etudiant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='affectation_set', to='promotions.Etudiant'),
        ),
        migrations.AlterField(
            model_name='affectation_etudiant',
            name='promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotion_set', to='promotions.Promotion'),
        ),
    ]
