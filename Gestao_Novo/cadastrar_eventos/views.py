from django.shortcuts import render, get_object_or_404,redirect
from .models import Evento
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    eventos = Evento.objects.all()
    dados = {
        'eventos' : eventos
    }
    return render(request, 'index.html', dados)

def cadastrar_eventos(request):
    if request.method == 'POST':
        grupo = request.POST['grupo']
        nome_evento = request.POST['nome_evento']
        descricao = request.POST['descricao']
        publico = request.POST['publico']
        qtd_convidados = request.POST['qtd_pessoas']
        foto_evento = request.FILES['foto_evento']
        user = get_object_or_404(User, pk=request.user.id)
        evento = Evento.objects.create(
            pessoa=user,
            grupo=grupo, 
            nome_evento=nome_evento, 
            descricao=descricao, 
            publico=publico, 
            convidados_qtd=qtd_convidados,
            img=foto_evento)
        evento.save()
        return redirect('dashboard')
    else:
        return render(request, 'cadastro_eventos.html')

def editar_eventos(request):
    pass

