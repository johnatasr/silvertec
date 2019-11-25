from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView , get_object_or_404
from rest_framework.decorators import action
from .models import Pedido, Computador, Memoria
from .permissions import IsOwnerOrReadOnly, IsAuthenticated
from .serializers import PedidoSerializer, ComputadorSerializer
from .pagination import CustomPagination


class pedidos_viewsets(ListCreateAPIView):
    serializer_class = PedidoSerializer
    # permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    queryset = Pedido.objects.all()

    def get_queryset(self):
        pedidos = Pedido.objects.all()
        return pedidos

    def get(self, request):
        pedidos = self.get_queryset()
        paginate_queryset = self.paginate_queryset(pedidos)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)


    def post(self, request):
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(comprador=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class pedido_viewset(RetrieveUpdateDestroyAPIView):
    serializer_class = PedidoSerializer
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    @action(methods=['GET'], detail=True)
    def get_queryset(self, id):
        try:
            pedido = Pedido.objects.get(id=id)
        except Pedido.DoesNotExist:
            content = {
                'status': 'Pedido não encotrado !'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return pedido


    def get(self, request, id):

        pedido = self.get_queryset(id)
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data, status=status.HTTP_200_OK)



class computadores_viewsets(ListCreateAPIView):
    serializer_class = ComputadorSerializer
    # permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination

    def get_queryset(self):
        computadores = Computador.objects.all()
        return computadores

    @action(methods=['GET'], detail=True)
    def get(self, request):
        computadores = self.get_queryset()
        paginate_queryset = self.paginate_queryset(computadores)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @action(methods=['POST'], detail=True)
    def post(self, request):

        data = request.data
        # teste = ", ".join([x for x in data['memorias']])

        if data['pl'][0] == '1' :
            if data['processador'][0] not in ('1', '2'):
                raise ValidationError("Placa Asus Prime só suporta processadores Intel !")
            else:
                if len(data['memorias']) > 2 :
                    raise ValidationError("Placa possui apenas 2 slots !")

                for memoria_id in data['memorias']:
                    memoria = Memoria.objects.get(id=memoria_id)
                    capacidade = memoria.capacidade

                if int(capacidade) > 16:
                    raise ValidationError("Placa suporta 16GB de Ram !")
                if data['vga'] is False:
                    raise ValidationError("Placa precisa de VGA ! ")

        elif data['pl'][0] == '2' :
            if data['processador'][0] not in ('4', '3'):
                raise ValidationError("Placa Gigabyte só suporta processadores AMD !")
            else:
                if len(data['memorias']) > 2 :
                    raise ValidationError("Placa possui apenas 2 slots !")

                for memoria_id in data['memorias']:
                    memoria = Memoria.objects.get(id=memoria_id)
                    capacidade = memoria.capacidade

                if int(capacidade) > 16:
                    raise ValidationError("Placa suporta 16GB de Ram !")
                if data['vga'] is False:
                    raise ValidationError("Placa precisa de VGA ! ")

        elif data['pl'][0] == '3' :
            if len(data['memorias']) > 4 :
                raise ValidationError("Placa possui apenas 4 slots !")

            for memoria_id in data['memorias']:
                memoria = Memoria.objects.get(id=memoria_id)
                capacidade = memoria.capacidade

            if int(capacidade) > 64:
                raise ValidationError("Placa suporta 64GB de Ram !")
        else:
            raise ValidationError("Nenhuma placa mãe selecionada !")


        serializer = ComputadorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class computador_viewset(RetrieveUpdateDestroyAPIView):
    serializer_class = ComputadorSerializer
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    @action(methods=['GET'], detail=True)
    def get_queryset(self, id):
        try:
            computador = Computador.objects.get(id=id)
        except Computador.DoesNotExist:
            content = {
                'status': 'Computador não existe'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return computador

    @action(methods=['GET'], detail=True)
    def get(self, request, id):

        computador = self.get_queryset(id)
        usuario = computador.usuario
        serializer = ComputadorSerializer(computador)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):

        computador = self.get_queryset(id)

        if (request.user == computador.usuario):
            serializer = Computador(computador, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'Sem autorização'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, id):

        computador = self.get_queryset(id)

        if (request.user == computador.usuario):  # If creator is who makes request
            computador.delete()
            content = {
                'status': 'Deletado !'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'Sem autorização ! '
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)






