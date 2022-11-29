from django.contrib import admin

from .models import Evento, Inscrito_Evento, Relatorio_Satisfacao
# Register your models here.

class ListandoEventos(admin.ModelAdmin):
    list_display = ('id','nome_evento', 'publico',)
    list_display_links = ('id', 'nome_evento')
    search_fields = ('nome_evento',)
    list_filter = ('publico',)
    list_per_page = 10

admin.site.register(Evento, ListandoEventos)

class ListaInscritos(admin.ModelAdmin):
    list_display = ('id', 'evento', 'inscrito')
    list_display_links = ('id', 'evento')

admin.site.register(Inscrito_Evento, ListaInscritos)

class Lista_Relatorios(admin.ModelAdmin):
    list_display = ('id', 'evento', 'inscrito', 'nota')
    list_display_links = ('id', 'evento')

admin.site.register(Relatorio_Satisfacao, Lista_Relatorios)
