from django.db import models
from django.contrib.auth.models import User

class Processador(models.Model):

    NOMES = (
        ('intel_core_i5', 'Intel Core i5'),
        ('intel_core_i7', 'Intel Core i7'),
        ('amd_atlhon', 'AMD Athlon'),
        ('amd_rysen7', 'AMD Rysen 7'),
    )

    MARCA = (('amd', 'AMD'), ('intel', 'Intel'))

    nome = models.CharField('Nome', max_length=20 ,blank=False, choices=NOMES)
    marca = models.CharField('Marca', max_length=20 ,blank=False, choices=MARCA)

class PlacaMae(models.Model):

    NOMES = (
       ('asus_prime', 'Asus Prime'),
       ('gigabyte', 'Gigabyte'),
       ('asrock_fatal', 'AsRock Fatal'),
    )

    SLOTS = (('2', '2'), ('4', '4'))

    nome = models.CharField(verbose_name='Nome Placa Mãe', max_length=20, null=False, choices=NOMES)
    slots = models.CharField(verbose_name='Slots Placa Mãe', max_length=20, null=False, choices=SLOTS)
    total_ram = models.CharField(verbose_name='Memória Total', max_length=20, null=False)
    video = models.BooleanField(verbose_name='Vídeo Integrado', null=False, default=False)

class Memoria(models.Model):

    CAP = (('4', '4'), ('8', '8'), ('16', '16'), ('32', '32'), ('64', '64'))

    marca = models.CharField(verbose_name='Marca Memória', max_length=20, null=False, default='Hyper X')
    capacidade = models.CharField(verbose_name='Capacidade', max_length=20, null=False, choices=CAP)

class Vga(models.Model):

    MODELO = (
        ('gigabyte_geforce_gtx_1060_6gb', 'Gigabyte Geforce GTX 1060 6GB'),
        ('pny_rtx_2060_6gb', 'PNY RTX 2060 6GB'),
        ('radeon_rx_580_8GB', 'Radeon RX 580 8GB')
    )

    modelo = models.CharField(verbose_name='Modelo', max_length=20, null=False, choices=MODELO)


class Computador(models.Model):

    processador = models.ForeignKey(Processador, on_delete=models.CASCADE, null=False)
    pl = models.ForeignKey(PlacaMae, on_delete=models.CASCADE, null=False)
    memorias = models.ManyToManyField(Memoria)
    vga = models.ForeignKey(Vga, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.id
#
class Pedido(models.Model):

    comprador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos')
    computadores = models.ManyToManyField(Computador)

