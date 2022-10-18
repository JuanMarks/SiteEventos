import mimetypes
import os
from random import randint
from django.contrib.auth.models import User
from datetime import date, datetime, timedelta, timezone
from django.shortcuts import render,HttpResponse, get_object_or_404, get_list_or_404, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.hashers import make_password
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import *
import pyexcel as p
from apps.arquivo_excel.models import Arquivo_excel
from apps.abstrair.funções import *
# Create your views here.

def mail(request, grupo):
    grupo = grupo.upper()
    if grupo != "ALL":
        data_user = Usuario.objects.all().filter(grupo=grupo)
        gp = comparar_grupos(grupo)
        usuario = {
            "usuario": data_user,
            "grupo": gp,
        }
    else:
        data_user = Usuario.objects.all()
        gp = comparar_grupos(grupo)
        usuario = {
            "usuario": data_user,
            "grupo": gp, 
        }
    return render(request, 'enviodeEmail.html', usuario)

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

def tela_recuperar_senha(request):
    return render(request, "recuperar_senha.html")

def recuperar_senha(request):
    # Verifica se o Metodo é Post
    if request.method == "POST":
        # Requisita o Email
        email_r = request.POST['email']
        if Usuario.objects.filter(email=email_r):
            # Trás todas os dados que tem o mesmo email
            usuario = RecuperarSenha.objects.filter(email_r=email_r)
            # Se existir ele vai deletar
            if usuario:
                usuario.delete()

            # Aqui ele vai criar o que precisa ser criado
            recuperar = RecuperarSenha()
            recuperar.email_r = email_r
            codigo = randint(0,999999)
            recuperar.codigo = codigo
            recuperar.data_vencimento = datetime.now(timezone.utc) + timedelta(minutes=1)
            recuperar.save()
            sla = get_object_or_404(RecuperarSenha, email_r=email_r)
            send_mail("Código de Recuperação", f"Aqui seu Código de Recuperação http://localhost:8000/novasenha/{sla.codigo}", 'ouvidoriaadocicafornasa@gmail.com', [f"{email_r}"])
            return redirect('login')
        else:
            return redirect('login')
    else:
        return redirect('login')

def nova_senha(request, codigo):
    verifica_codigo = RecuperarSenha.objects.filter(codigo=codigo)
    if verifica_codigo:
        codigo = get_object_or_404(RecuperarSenha, codigo=codigo)
        if not codigo.data_vencimento < datetime.now(timezone.utc):
            email_r = codigo.email_r
            usuario = get_object_or_404(Usuario, email=email_r)
            if request.method == "POST":
                senha = request.POST['senha']
                verifica_senha = request.POST['verifica_senha']
                if senha == verifica_senha:
                    usuario.senha = make_password(senha)
                    print('chegou aqui 1')
                    if not usuario.save():
                        apagar_mudar_senha = RecuperarSenha.objects.filter(email_r=email_r)
                        apagar_mudar_senha.delete()
                        print('chegou aqui 2')
                        return redirect('login')  
            return render(request, "novasenha.html")
        else:
            verifica_codigo.delete()
            return redirect('login')
    else:
        return redirect('login')