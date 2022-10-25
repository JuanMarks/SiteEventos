from apps.enviar.models import *
from django.shortcuts import render
from apps.abstrair.funções import *

def mail(request, grupo):
    grupo = grupo.upper()
    if grupo != "ALL":
        data_user = Usuario.objects.all().filter(grupo=grupo)
        gp = comparar_grupos(grupo)
        usuario = {
            "usuario": data_user,
            "grupo": gp,
        }
    else:
        data_user = Usuario.objects.all()
        gp = comparar_grupos(grupo)
        usuario = {
            "usuario": data_user,
            "grupo": gp, 
        }
    # empresas = 
    return render(request, 'enviodeEmail.html', usuario)
