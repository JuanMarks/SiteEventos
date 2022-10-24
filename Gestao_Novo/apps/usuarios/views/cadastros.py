from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from apps.enviar.models import Usuario
from apps.usuarios.models import Usuarios, Empresa

def criar_user(username, email, password, grupo):
    usuario = User.objects.create_user(username=username, email=email, password=password)
    usuario.groups.add(grupo)
    usuario.save()

def criar_grupos():
    groups = ['Usuarios Comuns', 'Empresa', 'ADM']
    [Group.objects.get_or_create(name=group) for group in groups]

def cadastro(request):
    if request.method == 'POST':
        nome_completo = request.POST['nome_completo']
        nome_usuario = request.POST['nome_usuario']
        telefone = request.POST['telefone']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        criar_grupos()
        
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
        
        grupo = Group.objects.get(name='Usuarios Comuns')
        criar_user(nome_usuario, email, senha, grupo)
        
        usuario = Usuarios.objects.create(
            nome_completo=nome_completo, 
            nome_usuario=nome_usuario, 
            telefone=telefone, 
            email=email,)
        usuario.save()
        usuario_bd = Usuario.objects.create(
            nome=nome_completo,
            e_mail=email,
        )
        usuario_bd.save()
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
        criar_grupos()
        if not nome.strip():
            print("O campo nome nao pode ficar em branco")
            return redirect('cadastro_empresa')

        if not email.strip():
            print("O campo email nao pode ficar em branco")
            return redirect('cadastro_empresa')
        
        if User.objects.filter(email=email).exists():
            print('usuario ja cadastrado')
            return redirect('cadastro_empresa')
        
        if senha == "":
            print('Senha nao pode ficar em branco')
            return redirect('cadastro_empresa')

        if senha_admin == "123456":
            if categoria == 'ADM':
                grupo = Group.objects.get(name='ADM')
        else:
            grupo = Group.objects.get(name='Empresa')
            empresa = Empresa.objects.create(nome_completo=nome, nome_empresa=nome_empresa, email=email, telefone=telefone)
            empresa.save()
        
        criar_user(nome, email, senha, grupo)
        return redirect('login')
    else:
        return render(request, 'cadastro_empresa.html')