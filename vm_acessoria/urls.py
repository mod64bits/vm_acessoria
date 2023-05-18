from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from apps.dashboard import urls as dashboard_urls
from apps.orcamentos import urls as orcamentos_urls
from apps.clientes import urls as cliente_urls
from apps.produtos import urls as produtos_urls
from apps.home import urls as home_urls
from apps.servicos import urls as servicos_url
from apps.propostas import urls as propostas_url
from apps.api import urls as api_urls

urlpatterns = [
    path('api/v1/', include(api_urls)),
    path('propostas/', include(propostas_url)),
    path('servicos/', include(servicos_url)),
    path('home/', include(home_urls)),
    path('orcamentos/', include(orcamentos_urls)),
    path('clientes/', include(cliente_urls)),
    path('produtos/', include(produtos_urls)),
    path('', include(dashboard_urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
