from rest_framework.serializers import ModelSerializer, ReadOnlyField, PrimaryKeyRelatedField
from django.contrib.auth.models import User
from silvertec.apps.pedidos.models import Computador, Processador, PlacaMae, Memoria, Vga, Pedido

class ComputadorSerializer(ModelSerializer):
    class Meta:
        model = Computador
        fields = "__all__"

class ProcessadorSerializer(ModelSerializer):
    class Meta:
        model = Processador
        fields = "__all__"

class PlSerializer(ModelSerializer):
    class Meta:
        model = PlacaMae
        fields = "__all__"

class MemoriaSerializer(ModelSerializer):
    class Meta:
        model = Memoria
        fields = "__all__"

class VgaSerializer(ModelSerializer):
    class Meta:
        model = Vga
        fields = "__all__"

class PedidoSerializer(ModelSerializer):
    creator = ReadOnlyField(source='comprador.username')

    class Meta:
        model = Pedido
        fields = "__all__"

class UserSerializer(ModelSerializer):
    movies = PrimaryKeyRelatedField(many=True, queryset=Pedido.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'pedidos')