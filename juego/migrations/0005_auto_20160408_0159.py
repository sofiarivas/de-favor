# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 01:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='categoria',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='juegos', to='juego.Categoria'),
        ),
    ]
