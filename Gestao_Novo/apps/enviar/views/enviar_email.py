from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, get_object_or_404
from apps.arquivo_excel.models import Arquivo_excel
from apps.abstrair.funções import *
from django.core.mail import EmailMultiAlternatives
from apps.enviar.models import *
import pyexcel as p
from datetime import datetime
from django.utils.html import strip_tags
from django.template.loader import render_to_string

def enviar(request):
    usuario = request.user.id
    usuario1 = get_object_or_404(User, pk = usuario)
    arquivo = Arquivo_excel.objects.all()
    salvar_excel = Arquivo_excel(arquivo=request.FILES['excel'])
    salvar_excel.save()
    if request.method == "POST":
        print(request.POST)
        if request.FILES['excel']:
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
            if '\n' in mensagem:
                mensagem = mensagem.split('\n')
            else:
                mensagem = [mensagem]

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
                mensagem = mensagem.split("\n")
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

            htmlcontent = render_to_string('envio.html', valores)
            convertido = strip_tags(htmlcontent)
            emailenviado = EmailMultiAlternatives(assunto, convertido, 'ouvidoriaadocicafornasa@gmail.com', [destinatarios[n]])
            emailenviado.attach_alternative(htmlcontent, 'text/html')
            emailenviado.send()
    return HttpResponse('Enviado')

def enviar_todos(request):
    usuario = request.user.id
    usuario1 = get_object_or_404(User, pk = usuario)
    if request.method == "POST":
        print(request.POST)
        if request.POST['selecionar']:
            selecionar = request.POST.getlist('selecionar')
            print(selecionar)
        if request.POST['assunto']:
            assunto = request.POST['assunto']
        if request.POST['imagem']:
            imagem = request.POST['imagem']
        if request.POST['mensagem']:
            mensagem = request.POST['mensagem']
            mensagem = mensagem.split("\n")
            print(mensagem)

    for user in selecionar:
        usuario = get_object_or_404(Usuario, pk=user)
        enviado = datetime.now()
        valores = {
            'usuario': usuario1.username,
            'assunto': assunto,
            'imagem': imagem,
            'mensagem': mensagem, 
            'enviado': enviado,
            'nome':usuario.nome
            }
        htmlcontent = render_to_string('envio.html', valores)
        print(htmlcontent)
        emailenviado = EmailMultiAlternatives(assunto, htmlcontent, 'ouvidoriaadocicafornasa@gmail.com', [usuario.e_mail])
        emailenviado.attach_alternative(htmlcontent, 'text/html')
        emailenviado.send(fail_silently=False)
    return HttpResponse('Enviado')