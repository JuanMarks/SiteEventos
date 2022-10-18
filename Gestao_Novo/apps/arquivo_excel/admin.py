from django.contrib import admin
from .models import Arquivo_excel
# Register your models here.
class Detalhes(admin.ModelAdmin):
    list_display = ['arquivo',]
admin.site.register(Arquivo_excel,Detalhes)