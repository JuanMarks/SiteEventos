from apps.cadastrar_eventos.models import Evento, Inscrito_Evento, Relatorio_Satisfacao
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User ,Group
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.core.paginator import Paginator
from django.db.models import Count, Avg

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
                events = Evento.objects.filter(id=inscrito.evento_id)
                eventos_lista = get_object_or_404(Evento, pk=inscrito.evento_id)
                lista_eventos.append(eventos_lista)
            
        elif grupos == 'ADM' or grupos == 'Empresa':
            lista_eventos = Evento.objects.filter(pessoa=id).order_by('-id')
        
        paginator = Paginator(lista_eventos, 3)
        page = request.GET.get('page')
        eventos = paginator.get_page(page)

        dados = {
            'eventos': eventos
        }
        return render(request, 'dashboard.html', dados)
    else:
        return redirect('login')

@login_required(login_url='login')
def tela_adm(request):
    eventos = Evento.objects.all().order_by('-id')

    # --- KPIs (agregações no banco, sem loops) ---
    total_eventos = eventos.count()
    total_publicados = eventos.filter(publicar='Publicado').count()
    total_nao_publicados = total_eventos - total_publicados
    total_inscritos = Inscrito_Evento.objects.count()
    total_usuarios = User.objects.count()
    nota_media_geral = Relatorio_Satisfacao.objects.aggregate(m=Avg('nota'))['m'] or 0
    nota_media_geral = round(nota_media_geral, 1)

    # --- Gráfico: inscritos por evento (top 8) ---
    inscritos_por_evento = (
        Evento.objects
        .annotate(total=Count('inscrito_evento'))
        .order_by('-total')[:8]
        .values('nome_evento', 'total')
    )
    insc_labels = [e['nome_evento'] for e in inscritos_por_evento]
    insc_data = [e['total'] for e in inscritos_por_evento]

    # --- Gráfico: distribuição de notas de satisfação ---
    dist_notas = (
        Relatorio_Satisfacao.objects
        .values('nota')
        .annotate(qtd=Count('id'))
        .order_by('nota')
    )
    notas_labels = [f"Nota {n['nota']}" for n in dist_notas]
    notas_data = [n['qtd'] for n in dist_notas]

    # --- Gráfico: eventos mais bem avaliados (top 5 por nota média) ---
    top_avaliados = (
        Evento.objects
        .filter(relatorios_feitos__gt=0)
        .order_by('-nota_media')[:5]
        .values('nome_evento', 'nota_media')
    )
    top_labels = [e['nome_evento'] for e in top_avaliados]
    top_data = [e['nota_media'] for e in top_avaliados]

    # --- Gráfico: usuários por grupo ---
    grupos = Group.objects.annotate(total=Count('user')).values('name', 'total')
    grupos_labels = [g['name'] for g in grupos]
    grupos_data = [g['total'] for g in grupos]

    dados = {
        'eventos': eventos,
        'kpis': {
            'total_eventos': total_eventos,
            'total_publicados': total_publicados,
            'total_nao_publicados': total_nao_publicados,
            'total_inscritos': total_inscritos,
            'total_usuarios': total_usuarios,
            'nota_media_geral': nota_media_geral,
        },
        'chart_publicacao': [total_publicados, total_nao_publicados],
        'chart_inscritos': {'labels': insc_labels, 'data': insc_data},
        'chart_notas': {'labels': notas_labels, 'data': notas_data},
        'chart_top': {'labels': top_labels, 'data': top_data},
        'chart_grupos': {'labels': grupos_labels, 'data': grupos_data},
    }

    return render(request, 'tela-adm.html', dados)


