from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from cadastrar_eventos.models import Evento, Inscrito_Evento
from .models import Usuarios, Empresa
from cadastrar_eventos.forms import Editar_Evento

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
        
        usuario1 = User.objects.create_user(username=nome_usuario, email=email, password=senha) 
        grupo = get_object_or_404(Group, name='Usuarios Comuns')
        usuario1.groups.add(grupo)
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
        categoria = request.POST['categoria']
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        senha = request.POST['password']
        senha_admin = request.POST['password-admin']

        if not nome.strip():
            print("O campo nome nao pode ficar em branco")
            return redirect('cadastro_empresa')
        
        if not email.strip():
            print("O campo email nao pode ficar em branco")
            return redirect('cadastro_empresa')
        
        if User.objects.filter(email=email).exists():
            print('usuario ja cadastrado')
            return redirect('cadastro_empresa')

        if senha_admin == "123456":
            if categoria == 'ADM':
                grupo = get_object_or_404(Group, name='ADM')
        else:
            grupo = get_object_or_404(Group, name='Empresa')
            empresa = Empresa.objects.create(nome_completo=nome, nome_empresa=nome_empresa, email=email, telefone=telefone)
            empresa.save()
        
        usuario1 = User.objects.create_user(username=nome, email=email, password=senha) 
        usuario1.groups.add(grupo)
        usuario1.save()
        
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

def tela_adm(request):
    eventos = Evento.objects.all()

    dados = {
        'eventos': eventos
    }

    return render(request, 'tela-adm.html', dados)

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

def apagar_evento(request, id):
    evento = get_object_or_404(Evento, pk=id)
    evento.delete()
    return redirect('tela_adm')