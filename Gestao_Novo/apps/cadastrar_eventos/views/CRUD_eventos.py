from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from ..forms import Editar_Evento
from django.contrib.auth.models import User
from ..models import Evento, Inscrito_Evento

@login_required(login_url='login')
def cadastrar_eventos(request):
    if request.method == 'POST':
        grupo = request.POST['grupo']
        nome_empresa = request.POST['nome_empresa']
        nome_evento = request.POST['nome_evento']
        descricao = request.POST['descricao']
        publico = request.POST['publico']
        data_inicio = request.POST['data_inicio']
        data_termino = request.POST['data_termino']
        qtd_convidados = request.POST['qtd_pessoas']
        foto_evento = request.FILES['foto_evento']
        user = get_object_or_404(User, pk=request.user.id)
        evento = Evento.objects.create(
            pessoa=user,
            grupo=grupo, 
            nome_empresa=nome_empresa,
            nome_evento=nome_evento, 
            descricao=descricao, 
            publico=publico,
            publicar='Não Publicado',
            data_inicio=data_inicio,
            data_termino = data_termino,
            convidados_qtd=qtd_convidados,
            img=foto_evento)
        evento.save()
        return redirect('dashboard')
    else:
        return render(request, 'cadastro_eventos.html')


@login_required(login_url='login')
def editar_evento(request, id):
    evento = get_object_or_404(Evento, pk=id)
    form = Editar_Evento(instance=evento)
    if request.method == 'POST':
        form = Editar_Evento(request.POST, instance=evento)
        if form.is_valid():
            evento.save()
            return redirect('tela_adm')
        else:
            return render(request, 'editar_evento.html', {'form': form, 'eventos': evento})
    else:
        return render(request, 'editar_evento.html', {'form': form, 'eventos': evento})

@login_required(login_url='login')
def apagar_evento(request, id):
    evento = get_object_or_404(Evento, pk=id)
    evento.delete()
    return redirect('tela_adm')

@login_required(login_url='login')
def inscrever_evento(request, id):
    inscrito = get_object_or_404(User, pk=request.user.id)
    evento = get_object_or_404(Evento, pk=id)
    
    inscrever = Inscrito_Evento.objects.create(evento=evento, inscrito=inscrito)
    inscrever.save()
    return redirect('index')