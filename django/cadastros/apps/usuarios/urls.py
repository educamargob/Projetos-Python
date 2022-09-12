from django.urls import path

from . import views

urlpatterns = [
    path('usuario/login', views.login_usuario, name='login_usuario'),
    path('usuario/cadastro', views.cadastro_usuario, name='cadastro_usuario'),
    path('usuario/logout', views.logout_usuario, name='logout_usuario')
]