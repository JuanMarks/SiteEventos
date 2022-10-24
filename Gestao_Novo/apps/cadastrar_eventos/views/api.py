from rest_framework import viewsets
from django.views.generic import ListView
from apps.cadastrar_eventos.serializers import EventoSerializer, Inscrito_EventoSerializer
from apps.cadastrar_eventos.models import Evento, Inscrito_Evento

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
