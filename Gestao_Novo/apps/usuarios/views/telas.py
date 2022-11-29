from apps.cadastrar_eventos.models import Evento, Inscrito_Evento
from django.shortcuts import render, redirect
from django.contrib.auth.models import User ,Group
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        grupo = Group.objects.filter(id=id)
        print(grupo)
        #if grupo.name == 'Usuarios Comuns':
        evento_id = get_object_or_404(Evento, id=id)
        inscrito = Inscrito_Evento.objects.filter(evento=evento_id)
        
        eventos2 = inscrito.evento_id
        print(eventos2)
        dados = {
            'eventos': evento_id 
        }
        return render(request, 'dashboard.html', dados)
    else:
        return redirect('login')

def tela_adm(request):
    eventos = Evento.objects.all()

    dados = {
        'eventos': eventos
    }

    return render(request, 'tela-adm.html', dados)


