# Generated by Django 4.0.6 on 2022-08-30 23:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrar_eventos', '0005_alter_evento_data_inicio_alter_evento_data_termino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data_inicio',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 8, 30, 20, 17, 27, 275266)),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_termino',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 8, 30, 20, 17, 27, 275266)),
        ),
    ]
