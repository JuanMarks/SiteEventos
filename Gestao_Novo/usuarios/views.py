from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from cadastrar_eventos.models import Evento, Inscrito_Evento
from .models import Usuarios, Empresa

# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        nome_completo = request.POST['nome_completo']
        nome_usuario = request.POST['nome_usuario']
        telefone = request.POST['telefone']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome_usuario.strip():
            print("O campo nome nao pode ficar em branco")
            return redirect('cadastro')
        
        if not email.strip():
            print("O campo email nao pode ficar em branco")
            return redirect('cadastro')
        
        if senha != senha2:
            print('As senhas nao estao iguais')
            return redirect('cadastro')
        
        if User.objects.filter(email=email).exists():
            print('usuario ja cadastrado')
            return redirect('cadastro')
        
        usuario1 = User.objects.create_user(username=nome_usuario, first_name='USR', email=email, password=senha) 
        usuario1.save()
        usuario = Usuarios.objects.create(
            nome_completo=nome_completo, 
            nome_usuario=nome_usuario, 
            telefone=telefone, 
            email=email,)
        usuario.save()
        return redirect('login')
    else:
        return render(request, 'cadastro.html')

def cadastro_empresa(request):
    if request.method == 'POST':
        nome_empresa = request.POST['nome_empresa']
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        senha = request.POST['password']

        if not nome.strip():
            print("O campo nome nao pode ficar em branco")
            return redirect('cadastro_empresa')
        
        if not email.strip():
            print("O campo email nao pode ficar em branco")
            return redirect('cadastro_empresa')
        
        if User.objects.filter(email=email).exists():
            print('usuario ja cadastrado')
            return redirect('cadastro_empresa')

        usuario1 = User.objects.create_user(username=nome, first_name='ADM', email=email, password=senha) 
        usuario1.save()
        empresa = Empresa.objects.create(nome_completo=nome, nome_empresa=nome_empresa, email=email, telefone=telefone)
        empresa.save()
        return redirect('login')
    else:
        return render(request, 'cadastro_empresa.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['username']
        senha = request.POST['senha']

        if email == "" or senha == "":
            print('Os campos email e senha nao podem ficar em branco')
            return redirect('index')
        #print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
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

def saibamais(request, id):
    evento = Evento.objects.filter(id=id)
    inscrito = Inscrito_Evento.objects.filter(evento=evento)
    dados = {
        'eventos' : evento,
        'inscritos': inscrito
    }

    return render(request, 'saibamais.html', dados)