from django.urls import include, path
from rest_framework import routers
from .servico_views import ServicoViewSet, CategoriaServicoViewSet

router = routers.DefaultRouter()
router.register(r'servicos/categorias', CategoriaServicoViewSet)
router.register(r'servicos', ServicoViewSet)

urlpatterns = [
    path('', include(router.urls)),

]