from django.core.files.base import ContentFile
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST
from .models import Pedido


class Pedidos(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]

    @action(methods=['POST'], detail=False)
    def criar_pedido(self, request):
        global status

        data = request.data
        user = request.user.id


        try:
            query_pedido = Pedido.objects.create(comprador_id=user)

            if len(data['pedido']['computadores']['processador']) > 1:
                msg = 'Só é permitido um processador por computador'
                status.append(msg)
            else:
                if data['pedido']['computadores']['processador']:
                    if data['pedido']['computadores']['processador']['nome'] == 'Intel Core i5' & 'Intel Core i7':
                        data['pedido']['computadores']['processador']['marca'] = 'Intel'
                    elif data['pedido']['computadores']['processador']['nome'] == 'AMD Athlon' & 'AMD Rysen 7':
                        data['pedido']['computadores']['processador']['marca'] = 'AMD'

                if data['pedido']['computadores']['placamae']:



                    if data['pedido']['computadores']['placamae']['nome'] == 'Asus Prime':
                        data['pedido']['computadores']['placamae']['slots'] = '2'
                        data['pedido']['computadores']['placamae']['total_ram'] = '32'
                        data['pedido']['computadores']['placamae']['video'] = False
                    elif data['pedido']['computadores']['placamae']['nome'] == 'Gigabyte':
                        data['pedido']['computadores']['placamae']['slots'] = '2'
                        data['pedido']['computadores']['placamae']['total_ram'] = '32'
                        data['pedido']['computadores']['placamae']['video'] = False
                    elif data['pedido']['computadores']['placamae']['nome'] == 'AsRock Fatal':
                        data['pedido']['computadores']['placamae']['slots'] = '4'
                        data['pedido']['computadores']['placamae']['total_ram'] = '64'
                        data['pedido']['computadores']['placamae']['video'] = True

                if data['pedido']['computadores']['memoria']:

                    capacidade =  data['pedido']['computadores']['memoria']['capacidade']
                    if data['pedido']['computadores']['memoria']['capacidade']


