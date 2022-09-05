from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_produtos', views.cadastro_produtos, name='cadastro_produtos'),
    path('produtos/criar', views.cria_produto, name='cria_produto'),
    path('produtos', views.mostra_produto, name='mostra_produto'),
    path('produtos/listar', views.lista_produtos, name='lista_produtos'),
]