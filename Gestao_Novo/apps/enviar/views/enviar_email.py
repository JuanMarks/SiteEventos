from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, get_object_or_404, render, redirect
from apps.arquivo_excel.models import Arquivo_excel
from apps.abstrair.funções import *
from apps.cadastrar_eventos.models import Evento, Inscrito_Evento
from django.core.mail import EmailMultiAlternatives, send_mail
from apps.enviar.models import *
import pyexcel as p
from datetime import datetime
from django.utils.html import strip_tags
from django.template.loader import render_to_string

def enviar(request):
    usuario = request.user.id
    usuario1 = get_object_or_404(User, pk = usuario)
    arquivo = Arquivo_excel.objects.all()
    if request.method == "POST":
        print(request.POST)
        if request.FILES != '':
            salvar_excel = Arquivo_excel(arquivo=request.FILES['excel'])
            salvar_excel.save()
            post_files = f"{request.FILES['excel']}"
            post_files = post_files.split(" ")
            post = f"{post_files[0]}_{post_files[1]}"
            print(post_files)
            diretorio = diretorio_excel(arquivo, post)
            print(diretorio)
            excel = p.get_sheet(file_name=diretorio)
            dados = pegar_dados(excel)
            
            destinatarios = dados['emails']
            nome = dados['nomes']

            assunto = request.POST['assunto']
            if request.POST['imagem']:
                imagem = request.POST['imagem']
            mensagem = request.POST['mensagem']

            print(mensagem)
        else:
            destinatarios = []

            destinatario = request.POST['destinatario']
            destinatarios = destinatario.split(",")
            destinatarios.strip

            assunto = request.POST['assunto']
            if request.POST['imagem']:
                imagem = request.POST['imagem']
            
            if request.POST['mensagem']:
                mensagem = request.POST['mensagem']
            print(mensagem)
            # else:
            #     mensagem = [mensagem]

        for n in range(len(destinatarios)):
            enviado = datetime.now()
            valores = {
                'usuario': usuario1.username,
                'assunto': assunto,
                'imagem': imagem,
                'mensagem': mensagem, 
                'enviado': enviado,
                'nome' : nome[n]
                }
            htmls = html(valores)

            emailenviado = EmailMultiAlternatives(assunto, htmls, 'ouvidoriaadocicafornasa@gmail.com', [destinatarios[n]])
            emailenviado.attach_alternative(htmls, 'text/html')
            emailenviado.send()
    return HttpResponse('Enviado')

def enviar_todos(request):
    usuario = request.user.id
    usuario1 = get_object_or_404(User, pk = usuario)
    if request.method == "POST":
        if request.POST['selecionar']:
            selecionar = request.POST.getlist('selecionar')
            print(selecionar)
        if request.POST['assunto']:
            assunto = request.POST['assunto']
        if request.POST['imagem']:
            imagem = request.POST['imagem']
        if request.POST['mensagem']:
            mensagem = request.POST['mensagem']

    for user in selecionar:
        usuario = get_object_or_404(User, pk=user)
        enviado = datetime.now()
        valores = {
            'usuario': usuario1.username,
            'assunto': assunto,
            'imagem': imagem,
            'mensagem': mensagem, 
            'enviado': enviado,
            'nome':usuario.username
            }
        
        htmls = html(valores)
        # print(htmls)

        emailenviado = EmailMultiAlternatives(assunto, htmls, 'ouvidoriaadocicafornasa@gmail.com', [usuario.email])
        emailenviado.attach_alternative(htmls, 'text/html')
        emailenviado.send(fail_silently=False)
    return HttpResponse('Enviado')


def enviar_por_eventos(request):
    usuario = request.user.id
    usuario1 = get_object_or_404(User, pk = usuario)
    if request.method == "POST":
        if request.POST['selecionar']:
            selecionar = request.POST.getlist('selecionar')
        if request.POST['assunto']:
            assunto = request.POST['assunto']
        if request.POST['imagem']:
            imagem = request.POST['imagem']
        if request.POST['mensagem']:
            mensagem = request.POST['mensagem']

    for user in selecionar:
        eventos = Evento.objects.all()
        usuarios_cadastrados = Inscrito_Evento.objects.filter(evento__in=user)
        for inscrito in usuarios_cadastrados:
            enviado = datetime.now()
            valores = {
                'usuario': usuario1.username,
                'assunto': assunto,
                'imagem': imagem,
                'mensagem': mensagem, 
                'enviado': enviado,
                'nome':inscrito.inscrito
                }
            
            htmls = html(valores)

            emailenviado = EmailMultiAlternatives(assunto, htmls, 'ouvidoriaadocicafornasa@gmail.com', [inscrito.inscrito.email])
            emailenviado.attach_alternative(htmls, 'text/html')
            emailenviado.send(fail_silently=False)
    return render(request, 'htmlvazio.html', {'inscritos':usuarios_cadastrados, 'eventos':eventos})

def enviar_relatorio(request, id):
    evento = get_object_or_404(Evento, pk=id)
    inscritos = Inscrito_Evento.objects.filter(evento=evento)

    for inscrito in inscritos:
        email_usr = inscrito.inscrito.email
        
        send_mail(f"Formulário de Satisfação do Evento: {inscrito.evento.nome_evento}", f"Avalie o evento por meio deste link http://localhost:8000/relatorio_satisfacao/{inscrito.evento.pk}", 'ouvidoriaadocicafornasa@gmail.com', [f"{email_usr}"])
    
    return redirect('tela_adm')
