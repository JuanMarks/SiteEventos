from apps.cadastrar_eventos.models import Evento, Inscrito_Evento
from django.shortcuts import render, redirect
from django.contrib.auth.models import User ,Group
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

def dashboard(request):
    if request.user.is_authenticated: 
        id = request.user.id
        grupo = get_object_or_404(Group, name="Usuarios Comuns")
        grupos = Group.objects.filter(user=id).values_list('name', flat=True).get()
        print(grupos)
        
        if grupos == 'Usuarios Comuns' or grupos == 'Mantenedores':
            
            evento_inscritos = Inscrito_Evento.objects.filter(inscrito=id)
            lista_eventos = []
            for inscrito in evento_inscritos:
                eventos = Evento.objects.filter(id=inscrito.evento_id)
                eventos_lista = get_object_or_404(Evento, pk=inscrito.evento_id)
                lista_eventos.append(eventos_lista)
            
        elif grupos == 'ADM' or grupos == 'Empresa':
            lista_eventos = Evento.objects.filter(pessoa=id)
            

        dados = {
            'eventos': lista_eventos
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


