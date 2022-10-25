from django import views
from django.urls import path
from .views import views
from .views.views import render_pdf_view ,CustomerListView, customer_render_pdf_view

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_eventos', views.cadastrar_eventos, name='cadastrar_eventos'),
    path('saibamais', views.saibamais, name='saibamais'),
    path('teste/<int:id>', render_pdf_view, name='teste'),
    path('teste2', CustomerListView.as_view(), name='teste2'),
    path('pdf/<id>/', customer_render_pdf_view, name='teste3'),
    path('inscrever/<int:id>', views.inscrever_evento, name='inscrever')
]