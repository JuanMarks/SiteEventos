from django import forms
from .models import Evento

class Editar_Evento(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome_evento', 'img', 'publicar', 'descricao', 'data_inicio', 'data_termino', 'publico', 'convidados_qtd']