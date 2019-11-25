from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST
from .models import Pedido, Computador, Processador, PlacaMae, Vga, Memoria
from apps.pedidos.serializers import ComputadorSerializer

# class Pedidos(viewsets.ModelViewSet):
#
#     # permission_classes = [IsAuthenticated]
#     @action(methods=['GET'], detail=True)
#     def mostra_pedidos(self):
#         pass
#
#
#
#     @action(methods=['POST'], detail=False)
#     def criar_pedido(self, request):
#         global status
#
#         data = request.data
#         user = request.user.id
#
#         try:
#
#             return Response(status=HTTP_200_OK)
#
#         except Exception as error:
#             return Response(error, status=HTTP_500_INTERNAL_SERVER_ERROR)

class ComputadoresViewset(viewsets.ModelViewSet):

    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        serializer_class = ComputadorSerializer
        computadores = Computador.objects.all()


    @action(methods=['GET'], detail=True)
    def mostra_computadores(self):

        data = []

        queryset = Computador.objects.all()
        serializer = ComputadorSerializer(queryset, many=True).data

        for computador in serializer:

            response = {
                'id': computador['id'],
                'usuario': computador['usuario'],
                'descricao': computador['descricao'],
                'processador': computador['processador'],
                'pl': computador['pl'],
                'memorias': computador['memorias'],
                'vga': computador['vga']
            }

            data.append(response)

        return Response(data, status=HTTP_200_OK)



    @action(methods=['POST'], detail=False)
    def cria_computador(self, request):
        global status

        msg = []
        data = request.data
        user = request.user.id

        try:
            query_computador = Computador.objects.create(usuario=user, descricao=data['computador']['descricao'],
                                                         processador=data['computador']['processador'], pl=data['computador']['pl'],
                                                         memorias=data['computador']['memorias'], vga=data['computador']['vga'])

            if len(data['computadores']['processador']) > 1:
                return Response(status="Cada computador suporta uma CPU !")
            else:
                if data['computadores']['pl'] == 'Asus Prime':
                    if data['compuatador']['processador']['nome'] != 'Intel Core i5' or 'Intel Core i7':
                        return Response(status="Placa Asus Prime só suporta processadores Intel !")
                    if len(data['compuatador']['memorias']) > 2 :
                        return Response(status="Placa possui apenas 2 slots !")
                    if sum(int(data['compuatador']['memorias']['capacidade'])) > 16:
                        return Response(status="Placa suporta 16GB de Ram !")
                    if data['compuatador']['vga'] is False:
                        return Response(status="Placa precisa de VGA ! ")
                elif data['compuatador']['pl'] == 'Gigabyte':
                    if data['compuatador']['processador']['nome'] != 'AMD Athlon' or 'AMD Rysen 7':
                        return Response(status="Placa Gigabyte só suporta processadores AMD !")
                    if len(data['compuatador']['memorias']) > 2 :
                       return Response(status="Placa possui apenas 2 slots !")
                    if sum(int(data['compuatador']['memorias']['capacidade'])) > 16:
                        return Response(status="Placa suporta 16GB de Ram !")
                    if data['compuatador']['vga'] is False:
                       return Response(status="Placa precisa de VGA ! ")
                elif data['compuatador']['pl'] == 'AsRock Fatal':
                    if len(data['compuatador']['memorias']) > 4 :
                       return Response(status="Placa possui apenas 4 slots !")
                    if sum(int(data['compuatador']['memorias']['capacidade'])) > 64:
                       return Response(status="Placa suporta 64GB de Ram !")
                else:
                    return Response(status="Nenhuma placa mãe selecionada !")

            query_computador.save()

            return Response(status=HTTP_200_OK)

        except Exception as error:
            return Response(error, status=HTTP_500_INTERNAL_SERVER_ERROR)