# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-20 02:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_populate_spotlights'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='spotlight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_spotlight', to='profiles.Spotlight'),
        ),
    ]
