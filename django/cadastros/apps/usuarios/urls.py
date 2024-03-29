from django.urls import path

from . import views

urlpatterns = [
    path('firebase-messaging-sw.js', views.ServiceWorkerView.as_view(), name='service_worker'),
    path('devices', views.devices, name='devices'),
    path('teste', views.testeee, name='teste'),
    path('notifica', views.teste, name='testenot'),
    path('usuario/login', views.login_usuario, name='login_usuario'),
    path('usuario/cadastro', views.cadastro_usuario, name='cadastro_usuario'),
    path('usuario/logout', views.logout_usuario, name='logout_usuario'),
    path('usuario', views.lista_usuarios, name='lista_usuarios'),
    path('usuario/altera/<int:usuario_id>', views.altera_usuario, name='altera_usuario'),
    path('usuario/deleta/<int:produto_id>', views.deleta_usuario, name='deleta_usuario'),
    path('notificacao/cadastro', views.cadastro_notificacao, name='cadastro_notificacao')
]