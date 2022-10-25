from django.views.generic import ListView, View
from ..serializers import EventoSerializer, Inscrito_EventoSerializer
from rest_framework import viewsets
from ..models import Evento, Inscrito_Evento
from apps.cadastrar_eventos import serializers
from django.core import serializers as sz
from django.http import JsonResponse

class CustomerListView(ListView):
    model = Evento
    template_name = 'teste0main.html'

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    ordering_fields = ['nome_evento',]
    search_fields = ['nome_evento',]

class InscritoViewSet(viewsets.ModelViewSet):
    queryset = Inscrito_Evento.objects.all()
    serializer_class = Inscrito_EventoSerializer
    ordering_fields = ['evento',]

class EventoView(View):
    def get(self,request):
        qs = Evento.objects.all()
        data = sz.serialize('json', qs)
        return JsonResponse({'data':data}, safe=False)
