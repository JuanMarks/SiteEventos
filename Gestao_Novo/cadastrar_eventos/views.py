from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Evento, Inscrito_Evento
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

