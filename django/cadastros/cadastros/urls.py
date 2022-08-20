from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('cadastro_clientes.urls')),
    path('admin/', admin.site.urls),
]
