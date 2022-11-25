from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from ..models import Evento, Inscrito_Evento
def index(request):
    id = request.user.id
    user = User.objects.filter(pk=id)
    eventos = Evento.objects.all()
    inscritos = Inscrito_Evento.objects.filter(inscrito__in=user)
    
    dados = {
        'inscritos': inscritos,
        'eventos' : eventos,
        'var': True
    }
    return render(request, 'index.html', dados)

def saibamais(request, id):
    evento = Evento.objects.filter(id=id)
    evento_id = get_object_or_404(Evento, id=id)
    inscrito = Inscrito_Evento.objects.filter(evento=evento_id)
    
    if len(inscrito) > 1:
        inscrito = get_list_or_404(Inscrito_Evento, evento=evento_id)
    
    dados = {
        'eventos' : evento,
        'inscritos': inscrito
    }

    return render(request, 'saibamais.html', dados)


@login_required(login_url='login')
def tela_adm(request):
    eventos = Evento.objects.all()

    dados = {
        'eventos': eventos
    }

    return render(request, 'tela-adm.html', dados)
