from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', include('cadastro_clientes.urls')),
    path('', include('usuarios.urls')),
    path('', include('produtos.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^webpush/', include('webpush.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)