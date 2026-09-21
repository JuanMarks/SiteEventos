from django.db import migrations


def criar_grupos(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    for nome in ['Usuarios Comuns', 'Empresa', 'ADM', 'Mantenedores']:
        Group.objects.get_or_create(name=nome)


def remover_grupos(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(
        name__in=['Usuarios Comuns', 'Empresa', 'ADM', 'Mantenedores']
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(criar_grupos, remover_grupos),
    ]
