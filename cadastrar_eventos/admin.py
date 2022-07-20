from django.contrib import admin

from .models import Evento
# Register your models here.

class ListandoEventos(admin.ModelAdmin):
    list_display = ('id','nome_evento', 'publico', 'habilitar_inscrever')
    list_display_links = ('id', 'nome_evento')
    search_fields = ('nome_evento',)
    list_filter = ('publico',)
    list_editable = ('habilitar_inscrever', )
    list_per_page = 10

admin.site.register(Evento, ListandoEventos)