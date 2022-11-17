from django import views
from django.urls import path
from apps.cadastrar_eventos import views
from .views import render_pdf_view, customer_render_pdf_view

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_eventos', views.cadastrar_eventos, name='cadastrar_eventos'),
    path('saibamais/<int:id>', views.saibamais, name='saibamais'),
    path('teste/<int:id>', render_pdf_view, name='teste'),
    path('pdf/<id>/', customer_render_pdf_view, name='teste3'),
    path('inscrever/<int:id>', views.inscrever_evento, name='inscrever')
]