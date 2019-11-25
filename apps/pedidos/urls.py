from django.urls import include, path, re_path
from rest_framework import routers
from . import views

app_name = 'pedidos'
router = routers.DefaultRouter()

urlpatterns = [
    path('pedidos/', views.pedidos_viewsets.as_view(), name='pedidos'),
    # re_path(r'^/pedidos/(?P<pk>[0-9]+)$',  views.pedido_viewset.as_view(), name='pedido'),
    path('pedidos/<int:id>',  views.pedido_viewset.as_view(), name='pedido_detalhe'),
    path('montar/', views.computadores_viewsets.as_view(), name='computadores_montar'),
    path('detalhar/<int:id>', views.computador_viewset.as_view(), name='computador_detalhe')
]