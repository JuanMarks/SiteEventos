# Generated by Django 4.1 on 2022-09-09 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enviar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='grupo',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]