from django.urls import path

from . import views

urlpatterns = [
    path('mail/', views.mail, name='email'),
    path('enviar/', views.enviar, name='enviar'),
    path('enviar_todos/', views.enviar_todos, name='enviar_todos')
]
