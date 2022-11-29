from apps.cadastrar_eventos.models import Evento, Inscrito_Evento
from django.shortcuts import render, redirect
from django.contrib.auth.models import User ,Group
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

def dashboard(request):
    if request.user.is_authenticated: 
        id = request.user.id
         
        #usr_gp = request.groups.user
        #print(usr_gp)
        grupo = get_object_or_404(Group, name="Usuarios Comuns")
        grupos = Group.objects.filter(user=id).values_list('name', flat=True).get()
        print(grupos)
        #print(groups)
        if grupos == 'Usuarios Comuns' or grupos == 'Mantenedores':
            #inscrito = get_object_or_404(Inscrito_Evento, inscrito=id)
            evento_inscritos = Inscrito_Evento.objects.filter(inscrito=id)
            #eventos = Evento.objects.filter(id__in=evento_inscritos)
            lista_eventos = []
            for inscrito in evento_inscritos:
                eventos = Evento.objects.filter(id=inscrito.evento_id)
                eventos_lista = get_object_or_404(Evento, pk=inscrito.evento_id)
                lista_eventos.append(eventos_lista)
                #print(inscrito.evento_id)
            
        elif grupos == 'ADM' or grupos == 'Empresa':
            lista_eventos = Evento.objects.filter(pessoa=id)
            #print(eventos)

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


