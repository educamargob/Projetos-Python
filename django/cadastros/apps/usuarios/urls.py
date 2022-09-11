from django.urls import path

from . import views

urlpatterns = [
    path('usuario/cadastro', views.cadastro_usuario, name='cadastro_usuario'),
]