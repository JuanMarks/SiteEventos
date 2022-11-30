from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here

def login(request):
    if request.method == 'POST':
        email = request.POST['username']
        senha = request.POST['senha']

        if email == "" or senha == "":
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            print('Os campos email e senha nao podem ficar em branco')
            return redirect('login')
        
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print("login realizado com sucesso")
                return redirect('index')
        else:
            messages.error(request, 'Usuario não cadastrado')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

