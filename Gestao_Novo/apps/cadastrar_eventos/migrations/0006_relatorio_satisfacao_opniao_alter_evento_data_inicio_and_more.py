# Generated by Django 4.1 on 2022-11-30 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrar_eventos', '0005_evento_soma_notas_alter_evento_data_inicio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatorio_satisfacao',
            name='opniao',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_inicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 30, 17, 26, 59, 547362)),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_termino',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 30, 17, 26, 59, 547362)),
        ),
    ]
