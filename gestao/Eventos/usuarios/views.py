from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from cadastrar_eventos.models import Evento

# Create your views here.

def cadastro(request):
    pass

def login(request):
    if request.method == 'POST':
        email = request.POST['username']
        senha = request.POST['senha']

        if email == "" or senha == "":
            print('Os campos email e senha nao podem ficar em branco')
            return redirect('index')
        print(email, senha)
        if User.objects.filter(username=email).exists():
            nome = User.objects.filter(username=email).values_list('username', flat=True).get()
            # senha = User.objects.filter(password=senha).values_list('password', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print("login realizado com sucesso")
                print(nome)
                return redirect('dashboard')
    return render(request, 'login.html')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        eventos = Evento.objects.filter(pessoa=id)

        dados = {
            'eventos': eventos
        }
        return render(request, 'dashboard.html', dados)
    else:
        return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('index')

def criar_evento(request):
    pass