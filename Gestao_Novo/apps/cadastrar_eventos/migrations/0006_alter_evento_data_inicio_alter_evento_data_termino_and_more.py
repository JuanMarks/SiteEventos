# Generated by Django 4.1 on 2022-11-24 00:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrar_eventos', '0005_remove_inscrito_evento_inscritos_evento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data_inicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 23, 21, 9, 2, 281031)),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_termino',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 23, 21, 9, 2, 281031)),
        ),
        migrations.AlterField(
            model_name='evento',
            name='inscritos_evento',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
