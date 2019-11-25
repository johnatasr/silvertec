from rest_framework.serializers import ModelSerializer, ReadOnlyField, PrimaryKeyRelatedField, ValidationError, StringRelatedField

from django.contrib.auth.models import User
from .models import Processador, PlacaMae, Memoria, Vga, Computador, Pedido


class ComputadorSerializer(ModelSerializer):
    usuario = ReadOnlyField(source='usuario.username')

    class Meta:
        model = Computador
        fields = ['id', 'usuario', 'descricao', 'processador', 'pl', 'memorias', 'vga']


    def validate(self, data):

        if data['processador'] :
            if data['pl'] == 1 :
                if data['processador'] != 1 or 4 :
                    raise ValidationError("Placa Asus Prime só suporta processadores Intel !")
                if len(data['memorias']) > 2 :
                    raise ValidationError("Placa possui apenas 2 slots !")
                if sum(int(data['memorias']['capacidade'])) > 16:
                    raise ValidationError("Placa suporta 16GB de Ram !")
                if data['vga'] is False:
                    raise ValidationError("Placa precisa de VGA ! ")
            elif data['pl'] == 2 :
                if data['processador'] != 'AMD Athlon' or 'AMD Rysen 7':
                    raise ValidationError("Placa Gigabyte só suporta processadores AMD !")
                if len(data['memorias']) > 2 :
                    raise ValidationError("Placa possui apenas 2 slots !")
                if sum(int(data['memorias']['capacidade'])) > 16:
                    raise ValidationError("Placa suporta 16GB de Ram !")
                if data['vga'] is False:
                    raise ValidationError("Placa precisa de VGA ! ")
            elif data['pl'] == 3 :
                if len(data['memorias']) > 4 :
                    raise ValidationError("Placa possui apenas 4 slots !")
                if sum(int(data['memorias']['capacidade'])) > 64:
                    raise ValidationError("Placa suporta 64GB de Ram !")
            else:
                raise ValidationError("Nenhuma placa mãe selecionada !")
        else:
           raise ValidationError("Necessário um processador para o compor o computador!")

        return data



class PedidoSerializer(ModelSerializer):
    comprador= ReadOnlyField(source='comprador.username')
    # computadores = ComputadorSerializer

    def validate(self, data):
        if data['computadores'] is False:
            raise ValidationError("Para fechar pedido é necessário pelo menos um computador !!")

    class Meta:
        model = Pedido
        fields = ('id', 'comprador', 'computadores')

class UserSerializer(ModelSerializer):
    pedidos = PrimaryKeyRelatedField(many=True, queryset=Pedido.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'pedidos')