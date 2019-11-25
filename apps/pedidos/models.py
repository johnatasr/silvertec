from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Processador(models.Model):

    NOMES = (
        ('Intel Core i5', 'Intel Core i5'),
        ('Intel Core i7', 'Intel Core i7'),
        ('Amd Atlhon', 'AMD Athlon'),
        ('Amd Rysen7', 'AMD Rysen 7'),
    )

    nome = models.CharField('Nome', max_length=20 ,blank=False, choices=NOMES)
    # marca = models.CharField('Marca', max_length=20 ,blank=False)


    def __str__(self):
        return self.nome

    def __unicode__(self):
        return '%s' % self.nome

class PlacaMae(models.Model):

    NOMES = (
       ('Asus Prime', 'Asus Prime'),
       ('Gigabyte', 'Gigabyte'),
       ('AsRock Fatal', 'AsRock Fatal'),
    )

    SLOTS = (('2', '2'), ('4', '4'))

    nome = models.CharField(verbose_name='Nome Placa Mãe', max_length=20, null=False, choices=NOMES)
    slots = models.CharField(verbose_name='Slots Placa Mãe', max_length=20, null=False, choices=SLOTS)
    total_ram = models.CharField(verbose_name='Memória Total', max_length=20, null=False)
    video = models.BooleanField(verbose_name='Vídeo Integrado', null=False, default=False)


    def __str__(self):
        return self.nome

    def __unicode__(self):
        return '%s' % self.nome

class Memoria(models.Model):

    CAP = (('4', '4'), ('8', '8'), ('16', '16'), ('32', '32'), ('64', '64'))

    capacidade = models.CharField(verbose_name='Capacidade', max_length=20, null=False, choices=CAP)

    def __str__(self):
        return 'Hyper X '+ self.capacidade + 'gb'

    def value(self):
        value = int(self.capacidade)
        return value

class Vga(models.Model):

    MODELO = (
        ('Gigabyte Geforce Gtx 1060 6gb', 'Gigabyte Geforce GTX 1060 6GB'),
        ('pny_rtx_2060_6gb', 'PNY RTX 2060 6GB'),
        ('radeon_rx_580_8GB', 'Radeon RX 580 8GB')
    )

    modelo = models.CharField(verbose_name='Modelo', max_length=50, null=False, choices=MODELO)

    def __str__(self):
        return self.modelo

    def __unicode__(self):
        return '%s' % self.modelo

class Compatibilidade(models.Model):

    processador_c = models.BooleanField(null=False, blank=False, default=False)
    memoria_c = models.BooleanField(null=False, blank=False, default=False)
    placa_mae_c = models.BooleanField(null=False, blank=False, default=False)
    vga_c = models.BooleanField(null=False, blank=False, default=False)


class Computador(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='computadores')
    descricao = models.CharField(max_length=100, blank=True, null=False)
    processador = models.ForeignKey(Processador, on_delete=models.CASCADE, null=False)
    pl = models.ForeignKey(PlacaMae, on_delete=models.CASCADE, null=False)
    memorias = models.ManyToManyField(Memoria, related_name='memorias')
    vga = models.ForeignKey(Vga, on_delete=models.CASCADE, null=False)


    class Meta:
        verbose_name = 'computador'
        verbose_name_plural = 'computadores'

    def __str__(self):
        return self.descricao


class Pedido(models.Model):

    comprador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos')
    computadores = models.ManyToManyField(Computador)

