# Generated by Django 4.1 on 2022-11-25 18:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastrar_eventos', '0009_remove_evento_inscritos_evento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='habilitar_importante',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='habilitar_inscrever',
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_inicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 25, 15, 27, 15, 150899)),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_termino',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 25, 15, 27, 15, 151895)),
        ),
        migrations.CreateModel(
            name='Relatorio_Satisfacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField(blank=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastrar_eventos.evento')),
                ('inscrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
