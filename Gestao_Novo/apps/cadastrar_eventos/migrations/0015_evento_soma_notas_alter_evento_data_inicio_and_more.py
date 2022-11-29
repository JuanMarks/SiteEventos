# Generated by Django 4.1 on 2022-11-25 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrar_eventos', '0014_evento_nota_media_alter_evento_data_inicio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='soma_notas',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_inicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 25, 15, 57, 15, 167132)),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_termino',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 25, 15, 57, 15, 167132)),
        ),
    ]
