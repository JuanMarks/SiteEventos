# Generated by Django 4.1 on 2022-11-29 12:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrar_eventos', '0002_alter_evento_data_inicio_alter_evento_data_termino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data_inicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 29, 9, 23, 40, 264316)),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_termino',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 29, 9, 23, 40, 264316)),
        ),
    ]