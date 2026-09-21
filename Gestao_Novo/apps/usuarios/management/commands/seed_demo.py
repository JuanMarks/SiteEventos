import random
from datetime import timedelta

from django.conf import settings
from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.cadastrar_eventos.models import Evento, Inscrito_Evento, Relatorio_Satisfacao


class Command(BaseCommand):
    help = 'Cria dados de demonstração para visualizar o app (somente com DEBUG=True).'

    def handle(self, *args, **options):
        if not settings.DEBUG:
            self.stderr.write(self.style.ERROR('Recusado: seed_demo só roda com DEBUG=True.'))
            return

        # Grupos
        for nome in ['Usuarios Comuns', 'Empresa', 'ADM', 'Mantenedores']:
            Group.objects.get_or_create(name=nome)
        adm_group = Group.objects.get(name='ADM')
        comum = Group.objects.get(name='Usuarios Comuns')

        # Admin de demonstração
        admin, _ = User.objects.get_or_create(username='admin', defaults={'email': 'admin@ninna.local'})
        admin.set_password('admin123')
        admin.is_staff = True
        admin.is_superuser = True
        admin.save()
        admin.groups.set([adm_group])

        # Usuários comuns
        comuns = []
        for i in range(1, 6):
            u, _ = User.objects.get_or_create(username=f'user{i}', defaults={'email': f'user{i}@ninna.local'})
            u.set_password('user123')
            u.save()
            u.groups.set([comum])
            comuns.append(u)

        # Eventos + inscrições + notas
        eventos_data = [
            ('Tech Summit', 'Aberto', 80),
            ('Workshop de Design', 'Aberto', 40),
            ('Meetup de Startups', 'Aberto', 60),
            ('Hackathon Ninna', 'Privado', 30),
        ]
        for nome, publico, qtd in eventos_data:
            ev, _ = Evento.objects.get_or_create(
                nome_evento=nome,
                defaults=dict(
                    pessoa=admin, grupo='STARTUP', nome_empresa='Ninna Hub',
                    data_inicio=timezone.now() + timedelta(days=random.randint(3, 30)),
                    data_termino=timezone.now() + timedelta(days=random.randint(31, 40)),
                    descricao=f'Descrição de demonstração do evento {nome}.',
                    publico=publico, convidados_qtd=qtd, publicar='Publicado',
                    relatorios_feitos=0, soma_notas=0, nota_media=0,
                ),
            )
            for u in random.sample(comuns, random.randint(2, 5)):
                Inscrito_Evento.objects.get_or_create(
                    evento=ev, inscrito=u, defaults={'nome': u.username, 'email': u.email})
                Relatorio_Satisfacao.objects.get_or_create(
                    evento=ev, inscrito=u, defaults={'nota': random.randint(6, 10), 'opniao': 'Muito bom'})

            notas = list(Relatorio_Satisfacao.objects.filter(evento=ev).values_list('nota', flat=True))
            if notas:
                ev.relatorios_feitos = len(notas)
                ev.soma_notas = sum(notas)
                ev.nota_media = round(sum(notas) / len(notas))
                ev.save()

        self.stdout.write(self.style.SUCCESS(
            'Seed concluído. Admin: admin / admin123 · Comuns: user1..user5 / user123 · 4 eventos publicados.'))
