from django.contrib import admin
from .models import Usuario

# Register your models here.
class Formatacao(admin.ModelAdmin):
    list_display = ('nome','e_mail',)
admin.site.register(Usuario,Formatacao)