from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from apps.enviar.models import RecuperarSenha
from random import randint
from datetime import datetime, timedelta, timezone
from django.core.mail import send_mail

# Create your views here.

def tela_recuperar_senha(request):
    return render(request, "recuperar_senha.html")

def recuperar_senha(request):
    # Verifica se o Metodo é Post
    if request.method != "POST":
        return redirect('login')

    email_r = request.POST['email']
    # Checa contra o User real do Django (fonte de verdade da autenticação).
    if not User.objects.filter(email=email_r).exists():
        # Não revela se o e-mail existe (evita enumeração de usuários).
        messages.success(request, 'Se o e-mail estiver cadastrado, enviaremos um código.')
        return redirect('login')

    # Remove códigos anteriores do mesmo e-mail.
    RecuperarSenha.objects.filter(email_r=email_r).delete()

    recuperar = RecuperarSenha()
    recuperar.email_r = email_r
    recuperar.codigo = randint(100000, 999999)
    recuperar.data_vencimento = datetime.now(timezone.utc) + timedelta(minutes=15)
    recuperar.save()

    link = f"{settings.SITE_URL}/enviar/novasenha/{recuperar.codigo}"
    send_mail(
        "Código de Recuperação",
        f"Use este link para redefinir sua senha (válido por 15 minutos): {link}",
        settings.DEFAULT_FROM_EMAIL,
        [email_r],
    )
    messages.success(request, 'Se o e-mail estiver cadastrado, enviaremos um código.')
    return redirect('login')

def nova_senha(request, codigo):
    codigo_qs = RecuperarSenha.objects.filter(codigo=codigo)
    if not codigo_qs.exists():
        return redirect('login')

    codigo_obj = get_object_or_404(RecuperarSenha, codigo=codigo)

    # Código expirado: limpa e volta.
    if codigo_obj.data_vencimento < datetime.now(timezone.utc):
        codigo_qs.delete()
        messages.error(request, 'Código expirado. Solicite um novo.')
        return redirect('login')

    user = User.objects.filter(email=codigo_obj.email_r).first()
    if user is None:
        codigo_qs.delete()
        return redirect('login')

    if request.method == "POST":
        senha = request.POST['senha']
        verifica_senha = request.POST['verifica_senha']
        if senha != verifica_senha:
            messages.error(request, 'As senhas não conferem.')
            return render(request, "novasenha.html")

        # Atualiza a senha real do usuário (corrige o bug: antes não alterava nada).
        user.set_password(senha)
        user.save()
        RecuperarSenha.objects.filter(email_r=codigo_obj.email_r).delete()
        messages.success(request, 'Senha alterada com sucesso. Faça login.')
        return redirect('login')

    return render(request, "novasenha.html")
