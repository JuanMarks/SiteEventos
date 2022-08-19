from django.contrib import admin
from .models import Usuarios
# Register your models here.

class ListandoUsuarios(admin.ModelAdmin):
    list_display = ('id', 'nome_usuario', 'email')
    list_display_links = ('id', 'nome_usuario')

admin.site.register(Usuarios, ListandoUsuarios)