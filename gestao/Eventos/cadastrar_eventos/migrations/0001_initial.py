# Generated by Django 4.0.6 on 2022-07-28 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_evento', models.CharField(max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('descricao', models.TextField()),
                ('publico', models.CharField(choices=[('Aberto', 'Aberto'), ('Privado', 'Privado')], max_length=20)),
                ('convidados_qtd', models.IntegerField()),
                ('habilitar_inscrever', models.BooleanField(default=False)),
                ('habilitar_importante', models.BooleanField(default=False)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cadastro_Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('nome_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastrar_eventos.evento')),
            ],
        ),
    ]