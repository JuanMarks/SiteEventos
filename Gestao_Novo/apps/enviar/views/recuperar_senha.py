from django.shortcuts import render, get_object_or_404, redirect
from apps.enviar.models import *
from random import randint
from datetime import datetime, timedelta, timezone
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.hashers import make_password

# Create your views here.

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