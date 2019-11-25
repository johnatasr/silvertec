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
        self.item_data = {
            'nome': 'Coca-Cola',
            'preco': 5
        }

    def test_criar_item(self):
        self.response = self.client.post(
            reverse('itemList'),
            self.item_data,
            format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_buscar_todos_items(self):
        itens = Item.objects.all()
        self.response = self.client.get(
            reverse('itemList'),
            format="json")
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertContains(self.response, itens)

    def test_apagar_item(self):
        refri = Item.objects.create(nome='Guarana', preco=7)
        response = self.client.delete(
            reverse('itemDel', kwargs={'item_pk': refri.id}),
            format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EntregaTestCase(TestCase):
    def setUp(self):
        self.pinheiro = Mercado.objects.create(nome='Pinheiro')
        refri = Item.objects.create(nome='Guarana', preco=7)
        self.pinheiro.estoque.add(refri)
        self.pinheiro.save()
        self.entrega = {
            'destino': 'Rua Francisco Segundo',
            'produtos': [refri.id],
            'total': 7,
            'data': str(timezone.now()),
            'remetente': self.pinheiro.id
        }

    def test_criar_entrega(self):
        response = self.client.post(
            reverse('entregaView'), self.entrega, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_buscar_entrega(self):
        entregas = Entrega.objects.all()
        self.response = self.client.get(
            reverse('entregaView'),
            format="json")

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertContains(self.response, entregas)

    def test_apagar_entrega(self):
        entregaDel = Entrega.objects.create(remetente=self.pinheiro, destino='Rua Francisco Segundo, 443.',
                                            data=timezone.now(), total=7)

        response = self.client.delete(
            reverse('entregaViewDel', kwargs={'entrega_pk': entregaDel.id}),
            format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MercadoTestCase(TestCase):
    def setUp(self):
        item = Item.objects.create(nome='Coca-Cola', preco=5)

        self.client = APIClient()
        self.mercado_data = {
            'nome': 'Pinheiro',
            'estoque': [item.id]
        }

    def test_criar_mercado(self):
        self.response = self.client.post(
            reverse('mercadoList'),
            self.mercado_data,
            format="json")

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_buscar_todos_mercados(self):
        mercados = Mercado.objects.all()
        self.response = self.client.get(
            reverse('mercadoList'),
            format="json")

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertContains(self.response, mercados)

    def test_buscar_mercado(self):
        pinheiro = Mercado.objects.create(nome='Pinheiro')
        response = self.client.get(
            reverse('mercadoPrincipal',
                    kwargs={'mercado_pk': pinheiro.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, MercadoSerializer(pinheiro).data)


from django.test import TestCase

# Create your tests here.
