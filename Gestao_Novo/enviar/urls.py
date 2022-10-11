from django.urls import path

from . import views

urlpatterns = [
    path('mail/<str:grupo>', views.mail, name='email'),
    path('enviar', views.enviar, name='enviar'),
    path('enviar_todos', views.enviar_todos, name='enviar_todos'),
    path('download_file/<str:filename>', views.download_file, name='download_file'),
    path('recuperar_senha', views.recuperar_senha, name='recuperar_senha')
]
