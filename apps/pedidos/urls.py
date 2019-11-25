from django.urls import include, path, re_path
from rest_framework import routers
from . import views

app_name = 'pedidos'
router = routers.DefaultRouter()

urlpatterns = [
    path('pedidos/', views.pedidos_viewsets.as_view(), name='Pedidos'),
    # path('pedidos/<int:id>', views.pedidos_viewsets.as_view(), name='Pedidos'),
    path('montar/', views.computadores_viewsets.as_view(), name='Montar Computadores')
    # path('listar/<int:id>', views.computadores_viewsets.as_view(), name='Montar Computadores')
]