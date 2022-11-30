from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.usuarios.models import Usuarios, Empresa
from apps.enviar.models import Usuario
from apps.usuarios.models import Usuarios, Empresa
from apps.enviar.models import Usuario
from apps.usuarios.models import Usuarios, Empresa

def criar_user(username, email, password, grupo):
    usuario = User.objects.create_user(username=username, email=email, password=password)
    usuario.groups.add(grupo)
    usuario.save()

def criar_grupos():
    groups = ['Usuarios Comuns', 'Empresa', 'ADM', 'Mantenedores']
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
            messages.error(request, 'O campo nome não pode ficar em branco')
            print("O campo nome nao pode ficar em branco")
            return redirect('cadastro')

        if not email.strip():
            messages.error(request, 'O campo email não pode ficar em branco')
            print("O campo email nao pode ficar em branco")
            return redirect('cadastro')
        
        if senha != senha2:
            messages.error(request, 'As senha nao sao iguais')
            print('As senhas nao estao iguais')
            return redirect('cadastro')
        
        if len(telefone) > 11:
            messages.error(request, 'Numero de telefone maior do que 11 digitos')
            return redirect('cadastro_empresa')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuario ja cadastrado')
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
        messages.success(request, 'Usuario cadastrado com sucesso')
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
            messages.error(request, 'O nome nao pode ficar em branco')
            print("O campo nome nao pode ficar em branco")
            return redirect('cadastro_empresa')

        if not email.strip():
            messages.error(request, 'Email nao pode ficar em branco')
            print("O campo email nao pode ficar em branco")
            return redirect('cadastro_empresa')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuario ja cadastrado')
            print('usuario ja cadastrado')
            return redirect('cadastro_empresa')
        
        if senha == "":
            messages.error(request, 'A senha nao pode ficar em branco')
            print('Senha nao pode ficar em branco')
            return redirect('cadastro_empresa')
        
        if len(telefone) > 11:
            messages.error(request, 'Numero de telefone maior do que 11 digitos')
            return redirect('cadastro_empresa')

        if categoria == 'Mantenedores':
            grupo = Group.objects.get(name='Mantenedores')
        
        if categoria == 'ADM':
            if senha_admin == "123456":
                grupo = Group.objects.get(name='ADM')
        else:
            grupo = Group.objects.get(name='Empresa')
            empresa = Empresa.objects.create(nome_completo=nome, nome_empresa=nome_empresa, email=email, telefone=telefone)
            empresa.save()
        
        criar_user(nome, email, senha, grupo)
        messages.success(request, 'Usuario cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'cadastro_empresa.html')