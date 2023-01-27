from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from apps.dashboard import urls as dashboard_urls
from apps.orcamentos import urls as orcamentos_urls
from apps.clientes import urls as cliente_urls

urlpatterns = [
    path('orcamentos/', include(orcamentos_urls)),
    path('clientes/', include(cliente_urls)),
    path('', include(dashboard_urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
