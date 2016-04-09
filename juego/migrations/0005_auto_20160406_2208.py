# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='categoria',
            field=models.CharField(choices=[('accion', 'Accion'), ('aventura', 'Aventura'), ('carreras', 'Carreras'), ('clasicos', 'Clasicos'), ('terror', 'Terror')], max_length=200),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
