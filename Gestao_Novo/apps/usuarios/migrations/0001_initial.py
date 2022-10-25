# Generated by Django 4.1 on 2022-10-24 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=200)),
                ('nome_empresa', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100)),
                ('nome_usuario', models.CharField(max_length=40)),
                ('telefone', models.CharField(max_length=20)),
                ('grupo', models.CharField(max_length=30)),
                ('nome_empresa', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
