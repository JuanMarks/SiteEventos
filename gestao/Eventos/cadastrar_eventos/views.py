from django.shortcuts import render
from .models import Evento

# Create your views here.

def index(request):
    eventos = Evento.objects.all()
    dados = {
        'eventos' : eventos
    }
    return render(request, 'index.html', dados)

