from django.urls import path

from . import views

urlpatterns = [
    path('usuario/login', views.login_usuario, name='login_usuario'),
    path('usuario/cadastro', views.cadastro_usuario, name='cadastro_usuario'),
    path('usuario/logout', views.logout_usuario, name='logout_usuario'),
    path('usuario', views.lista_usuarios, name='lista_usuarios'),
    path('usuario/altera/<int:usuario_id>', views.altera_usuario, name='altera_usuario'),
    path('usuario/deleta/<int:produto_id>', views.deleta_usuario, name='deleta_usuario'),
]