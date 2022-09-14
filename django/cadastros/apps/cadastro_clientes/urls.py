from django.urls import path

from . import views

urlpatterns = [
    path('clientes', views.lista_clientes, name='lista_clientes'),
    path('clientes/cadastrar', views.cadastro_clientes, name='cadastro_clientes'),
    path('clientes/altera/<int:cliente_id>', views.altera_cliente, name='altera_cliente'),
    path('clientes/deleta/<int:cliente_id>', views.deleta_cliente, name='deleta_cliente'),
]