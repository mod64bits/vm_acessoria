from rest_framework import viewsets
from apps.servicos.models import Servico, CategoriaServico
from .servico_serializers import CategoriaServicoserializers, ServicoSerializers


class CategoriaServicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint Categoria Serviços.
    """
    queryset = CategoriaServico.objects.all()
    serializer_class = CategoriaServicoserializers


class ServicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint Serviços.
    """
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializers
