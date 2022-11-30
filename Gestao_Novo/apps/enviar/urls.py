from django.urls import path

from . import views

urlpatterns = [
    path('mail/<str:grupo>', views.mail, name='email'),
    path('enviar/', views.enviar, name='enviar'),
    path('enviar_todos', views.enviar_todos, name='enviar_todos'),
    path('download_file/<str:filename>', views.download_file, name='download_file'),
    path('telarecuperarsenha/', views.tela_recuperar_senha, name='tela_recuperar_senha'), 
    path('recuperarsenha/', views.recuperar_senha, name="recuperar_senha"),
    path('novasenha/<int:codigo>', views.nova_senha, name='nova_senha'),
    path('enviar_relatorio/<int:id>', views.enviar_relatorio, name='enviar_relatorio'),
]
