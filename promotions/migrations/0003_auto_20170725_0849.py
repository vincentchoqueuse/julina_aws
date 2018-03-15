# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0002_auto_20170725_0545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modification', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moyenne', models.FloatField()),
                ('bulletin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promotions.Bulletin')),
            ],
        ),
        migrations.AddField(
            model_name='affectation_etudiant',
            name='bulletin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='promotions.Bulletin'),
            preserve_default=False,
        ),
    ]
