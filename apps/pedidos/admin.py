from django.contrib import admin
from apps.pedidos.models import Vga, Memoria, PlacaMae, Processador, Computador, Pedido

# admin.site.register(Pedidos)
admin.site.register(Vga)
admin.site.register(Memoria)
admin.site.register(PlacaMae)
admin.site.register(Processador)

admin.site.register(Computador)
admin.site.register(Pedido)
