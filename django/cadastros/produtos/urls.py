from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/<int:produto_id>', views.produto, name='produto'),
    path('cadastro_produtos', views.cadastro_produtos, name='cadastro_produtos'),
    path('produtos/criar', views.cria_produto, name='cria_produto'),
    path('produtos/listar', views.lista_produtos, name='lista_produtos'),
    path('produtos/altera/<int:produto_id>', views.altera_produto, name='altera_produto'),
    path('produtos/deleta/<int:produto_id>', views.deleta_produto, name='deleta_produto'),
]