from django.shortcuts import render, get_list_or_404
from apps.abstrair.funções import *
from apps.cadastrar_eventos.models import Evento
from django.contrib.auth.models import User, Group

def mail(request, grupo):
    eventos =  Evento.objects.all()
    if grupo != "all":
        data_user = User.objects.filter(groups = grupo)
        gp = Group.objects.all()
        usuario = {
            "usuario": data_user,
            "grupo": gp,
            "parametro": int(grupo.strip()),
            "eventos": eventos
        }
    else:
        data_user = User.objects.all()
        gp = Group.objects.all()
        usuario = {
            "usuario": data_user,
            "grupo": gp,
            "parametro": grupo.strip(),
            "eventos": eventos
        }
    return render(request, 'enviodeEmail.html', usuario)
