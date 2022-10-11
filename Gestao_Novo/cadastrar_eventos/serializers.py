from rest_framework import serializers
from .models import Evento, Inscrito_Evento

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class Inscrito_EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscrito_Evento
        fields = '__all__'
