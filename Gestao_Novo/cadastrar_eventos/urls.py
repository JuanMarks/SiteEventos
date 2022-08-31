from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_eventos', views.cadastrar_eventos, name='cadastrar_eventos'),
    path('saibamais/<int:id>', views.saibamais, name='saibamais'),
]