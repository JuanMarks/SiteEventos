from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from ..forms import Editar_Evento
from django.contrib.auth.models import User
from ..models import Evento, Inscrito_Evento, Relatorio_Satisfacao
from django.contrib import messages
from datetime import datetime

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

        data_hoje = str(datetime.now())
        #data = data_hoje.strftime("Y%/%m/%d %H:%M")
        #print(date)
        if data_inicio < data_hoje:
            messages.error(request, 'Data de inicio menor que data de hoje')
            return redirect('cadastrar_eventos')
        
        if int(qtd_convidados) > 100:
            messages.error(request, 'Quantidades de convidados maior do que a maxima')
            return redirect('cadastrar_eventos')
        


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
            img=foto_evento,
            relatorios_feitos=1)
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
    evento_inscricao = Evento.objects.filter(id=id)
    verificar_email = request.user.email
    if request.method == 'POST':
        inscrito = get_object_or_404(User, pk=request.user.id)
        evento = get_object_or_404(Evento, pk=id)
        nome = request.POST['nome']
        email = request.POST['email']

        if email != verificar_email:
            messages.error(request, 'Email diferente do usuario')
            return redirect('index')
            
        inscrever = Inscrito_Evento.objects.create(evento=evento, inscrito=inscrito, nome=nome, email=email)
        inscrever.save()
        
        return redirect('index')
    else:
        return redirect('tela-adm')

def remover_inscricao(request,id):
    usuario = request.user.id
    inscrito = Inscrito_Evento.objects.filter(pk=id)
    inscrito.delete()
    return redirect('index')

def tela_relatorio_satisfacao(request, id):
    if request.method == 'POST':
        relatorios_feitos = Evento.objects.filter(id=id).values_list('relatorios_feitos', flat=True).get()
        inscrito = get_object_or_404(User, pk=request.user.id)
        evento_form = get_object_or_404(Evento, pk=id)
        evento = Evento.objects.filter(id=id)
        nota = request.POST['nota']
        soma_notas = Evento.objects.filter(id=id).values_list('soma_notas',flat=True).get()
        soma = int(nota) + int(soma_notas)
        evento.update(soma_notas=soma)
        relatorio = Relatorio_Satisfacao.objects.create(evento=evento_form, inscrito=inscrito, nota=nota)
        evento.update(relatorios_feitos=int(relatorios_feitos) + 1)
        print(int(relatorios_feitos))
        evento.update(nota_media=soma/relatorios_feitos)

        
        
        return redirect('index')
    else:
        return render(request,'relatorio_satisfacao.html')