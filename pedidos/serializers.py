from rest_framework import serializers
from pedidos.models import Cliente, Pedido, ItensPedido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ItensPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = '__all__'
