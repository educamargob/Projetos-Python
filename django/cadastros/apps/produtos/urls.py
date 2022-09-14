from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produto/<int:produto_id>', views.produto, name='produto'),
    path('produto/cadastro', views.cadastro_produtos, name='cadastro_produtos'),
    path('produto/criar', views.cria_produto, name='cria_produto'),
    path('produto/listar', views.lista_produtos, name='lista_produtos'),
    path('produto/altera/<int:produto_id>', views.altera_produto, name='altera_produto'),
    path('produto/deleta/<int:produto_id>', views.deleta_produto, name='deleta_produto'),
]