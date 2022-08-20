from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_clientes', views.cadastro_clientes, name='cadastro_clientes'),
    path('cria/cliente', views.cria_cliente, name='cria_cliente'),
    path('clientes', views.mostra_cliente, name='mostra_cliente'),
]