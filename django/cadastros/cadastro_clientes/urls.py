from django.urls import path

from . import views

urlpatterns = [
    path('cadastro_clientes', views.cadastro_clientes, name='cadastro_clientes'),
    path('clientes/criar', views.cria_cliente, name='cria_cliente'),
    path('clientes', views.mostra_cliente, name='mostra_cliente'),
    path('clientes/listar', views.lista_clientes, name='lista_clientes'),
]