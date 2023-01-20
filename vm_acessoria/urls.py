from django.contrib import admin
from django.urls import path, include
from apps.dashboard import urls as dashboard_urls
from apps.orcamentos import urls as orcamentos_urls

urlpatterns = [
    path('orcamentos/', include(orcamentos_urls)),
    path('', include(dashboard_urls)),
    path('admin/', admin.site.urls),
]
