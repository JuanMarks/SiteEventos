import mimetypes
import os
from django.contrib.auth.models import User
from datetime import date, datetime
from django.shortcuts import render,HttpResponse, get_object_or_404, get_list_or_404
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Usuario
import pyexcel as p
from arquivo_excel.models import Arquivo_excel
from abstrair.funcoes import diretorio_excel,pegar_dados
# Create your views here.

def mail(request, grupo):
    grupo = grupo.upper()
    if grupo != "ALL":
        print(grupo)
        data_user = Usuario.objects.all().filter(grupo=grupo)
        usuario = {
            "usuario": data_user,
        }
    else:
        data_user = Usuario.objects.all()
        usuario = {
            "usuario": data_user,
        }
    return render(request, 'enviodeEmail.html', usuario)

def enviar(request):
    usuario = request.user.id
    usuario1 = get_object_or_404(User, pk = usuario)
    arquivo = Arquivo_excel.objects.all()
    salvar_excel = Arquivo_excel(arquivo=request.FILES['excel'])
    salvar_excel.save()
    if request.method == "POST":
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
        # send_mail(assunto, mensagem, remetente, destinatario)
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
    # send_mail(assunto, mensagem, remetente, destinatario)
    return HttpResponse('Enviado')

def download_file(request, filename=''):
    if filename != '':
        data = datetime.now()
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '/templates/static/excel/' + filename
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % f"{data}.xlsx"
        return response
    else:
        return render(request, 'file.html')