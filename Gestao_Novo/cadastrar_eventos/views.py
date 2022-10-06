from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Evento, Inscrito_Evento
from django.contrib.auth.models import User
from django.views.generic import ListView, View
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from rest_framework import viewsets, filters
from .serializers import EventoSerializer, Inscrito_EventoSerializer

# Create your views here.

def index(request):
    eventos = Evento.objects.all()
    dados = {
        'eventos' : eventos
    }
    return render(request, 'index.html', dados)

def cadastrar_eventos(request):
    if request.method == 'POST':
        grupo = request.POST['grupo']
        nome_empresa = request.POST['nome_empresa']
        nome_evento = request.POST['nome_evento']
        descricao = request.POST['descricao']
        publico = request.POST['publico']
        data_inicio = request.POST['data_inicio']
        data_termino = request.POST['data_termino']
        qtd_convidados = request.POST['qtd_pessoas']
        foto_evento = request.FILES['foto_evento']
        user = get_object_or_404(User, pk=request.user.id)
        evento = Evento.objects.create(
            pessoa=user,
            grupo=grupo, 
            nome_empresa=nome_empresa,
            nome_evento=nome_evento, 
            descricao=descricao, 
            publico=publico,
            publicar='Não Publicado',
            data_inicio=data_inicio,
            data_termino = data_termino,
            convidados_qtd=qtd_convidados,
            img=foto_evento)
        evento.save()
        return redirect('dashboard')
    else:
        return render(request, 'cadastro_eventos.html')

def saibamais(request, id):
    evento = Evento.objects.filter(id=id)
    evento_id = get_object_or_404(Evento, id=id)
    inscrito = Inscrito_Evento.objects.filter(evento=evento_id)
    
    if len(inscrito) > 1:
        inscrito = get_list_or_404(Inscrito_Evento, evento=evento_id)
    
    dados = {
        'eventos' : evento,
        'inscritos': inscrito
    }

    return render(request, 'saibamais.html', dados)

class CustomerListView(ListView):
    model = Evento
    template_name = 'teste0main.html'

def customer_render_pdf_view(request, *args, **kwargs):
    id = kwargs.get('id')
    evento = Evento.objects.filter(id=id)
    evento_id = get_object_or_404(Evento, id=id)
    inscrito = Inscrito_Evento.objects.filter(evento=evento_id)
    evento = get_object_or_404(Evento, id=id)
    a = len(inscrito)
    if len(inscrito) > 1:
        inscrito = get_list_or_404(Inscrito_Evento, evento=evento_id)

    template_path = 'teste0pdf.html'
    context = {
            'eventos' : evento,
            'inscritos': inscrito,
            'as': a
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #if diplay:
    response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>',context)
    return response

def render_pdf_view(request, id):
    evento = Evento.objects.filter(id=id)
    evento_id = get_object_or_404(Evento, id=id)
    inscrito = Inscrito_Evento.objects.filter(evento=evento_id)
    evento = get_object_or_404(Evento, id=id)
    a = len(inscrito)
    if len(inscrito) > 1:
        inscrito = get_list_or_404(Inscrito_Evento, evento=evento_id)

    template_path = 'teste0pdf.html'
    context = {
            'eventos' : evento,
            'inscritos': inscrito,
            'as': a
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #if diplay:
    response['Content-Disposition'] = 'filename="relatorio.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>',context)
    return response

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    ordering_fields = ['nome_evento',]
    search_fields = ['nome_evento',]

class InscritoViewSet(viewsets.ModelViewSet):
    queryset = Inscrito_Evento.objects.all()
    serializer_class = Inscrito_EventoSerializer
    ordering_fields = ['evento',]
