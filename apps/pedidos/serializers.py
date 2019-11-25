from rest_framework.serializers import ModelSerializer, ReadOnlyField, PrimaryKeyRelatedField

from django.contrib.auth.models import User
from .models import Processador, PlacaMae, Memoria, Vga, Computador, Pedido

class ComputadorSerializer(ModelSerializer):
    class Meta:
        model = Computador
        fields = ['id', 'usuario', 'descricao', 'processador', 'pl', 'memorias', 'vga']


class PedidoSerializer(ModelSerializer):

    class Meta:
        model = Pedido
        fields = ('id', 'comprador', 'computadores')

class UserSerializer(ModelSerializer):
    pedidos = PrimaryKeyRelatedField(many=True, queryset=Pedido.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'pedidos')