from rest_framework import serializers
from apps.servicos.models import Servico, CategoriaServico


class CategoriaServicoserializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriaServico
        fields = '__all__'


class ServicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'

