from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from .models import *
from .serializers import *
from django.utils import timezone


class ComputadorTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.computador_data = {
         "usuario": 1,
         "descricao": "teste",
         "processador": 2,
         "pl": 3,
         "memorias": [
             3
         ],
         "vga": 2
        },


    def test_criar_computador(self):
        self.response = self.client.post(
            reverse('itemList'),
            self.computador_data,
            format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_buscar_todos_computadores(self):
        computadores = Computador.objects.all()
        self.response = self.client.get(
            reverse('itemList'),
            format="json")
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertContains(self.response, computadores)



class PedidosTestCase(TestCase):
    def setUp(self):
        self.pinheiro = Mercado.objects.create(nome='Pinheiro')
        refri = Item.objects.create(nome='Guarana', preco=7)
        self.pinheiro.estoque.add(refri)
        self.pinheiro.save()
        self.entrega = {
            "comprador": 1,
            "computadores": [
                1, 2
            ]
        }
    def test_criar_pedido(self):
        response = self.client.post(
            reverse('entregaView'), self.entrega, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_buscar_pedido(self):
        entregas = Entrega.objects.all()
        self.response = self.client.get(
            reverse('entregaView'),
            format="json")

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertContains(self.response, entregas)


