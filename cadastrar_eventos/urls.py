from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/', views.eventos, name='eventos'),
    path('view_evento/', views.view_evento, name='view_evento'),
    path('formAvaliacao', views.formAvaliacao, name='formAvaliacao')
]
