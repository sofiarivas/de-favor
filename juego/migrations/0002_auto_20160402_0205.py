# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='plataforma',
            field=models.CharField(choices=[('ps2', 'Playstation 2'), ('ps3', 'Playstation 3'), ('ps4', 'Playstation 4'), ('wii', 'Nintendo Wii'), ('xbox', 'Xbox'), ('xbox360', 'Xbox 360'), ('xboxone', 'Xbox One')], db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='juego',
            name='ubicacion',
            field=models.CharField(choices=[('AGU', 'Aguascalientes'), ('BCN', 'Baja California'), ('BCS', 'Baja California Sur'), ('CAM', 'Campeche'), ('CDMX', 'Ciudad de Mexico'), ('CHH', 'Chihuahua'), ('CHP', 'Chiapas'), ('COA', 'Coahuila'), ('COL', 'Colima'), ('DUR', 'Durango'), ('GRO', 'Guerrero'), ('GUA', 'Guanajuato'), ('HID', 'Hidalgo'), ('JAL', 'Jalisco'), ('MEX', 'Estado de México'), ('MIC', 'Michoacán'), ('MOR', 'Morelos'), ('NAY', 'Nayarit'), ('NLE', 'Nuevo León'), ('OAX', 'Oaxaca'), ('PUE', 'Puebla'), ('QUE', 'Querétaro'), ('ROO', 'Quintana Roo'), ('SIN', 'Sinaloa'), ('SLP', 'San Luis Potosí'), ('SON', 'Sonora'), ('TAB', 'Tabasco'), ('TAM', 'Tamaulipas'), ('TLA', 'Tlaxcala'), ('VER', 'Veracruz'), ('YUC', 'Yucatán'), ('ZAC', 'Zacatecas')], max_length=100),
        ),
    ]