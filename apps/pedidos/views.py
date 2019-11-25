from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView , get_object_or_404
from rest_framework.views import APIView
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
        serializer = ComputadorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







