from django.shortcuts import render
from .models import Evento
# Create your views here.

def index(request):
    return render(request,'index.html')

def eventos(request):
    eventos = Evento.objects.all()
    dados = {
        'eventos' : eventos
    }
    return render(request, 'eventos.html', dados)

def view_evento(request):
    return render(request, 'view_evento.html')

def formAvaliacao(request):
    return render(request, 'formAvaliacao.html')