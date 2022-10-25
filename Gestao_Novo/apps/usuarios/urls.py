from django.urls import path
from apps.cadastrar_eventos.views import views as views_eventos
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('cadastro_empresa', views.cadastro_empresa, name='cadastro_empresa'),
    path('tela_adm', views.tela_adm, name='tela_adm'),
    path('editar_evento/<int:id>', views_eventos.editar_evento, name='editar_evento'),
    path('apagar_evento/<int:id>', views_eventos.apagar_evento, name='apagar_evento'),
    path('saibamais/<int:id>', views_eventos.saibamais, name='saibamais'),
]