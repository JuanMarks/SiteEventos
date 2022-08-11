from django.urls import path

from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('criar_evento', views.criar_evento, name='criar_evento'),
    path('cadastro_empresa', views.cadastro_empresa, name='cadastro_empresa')
    
]