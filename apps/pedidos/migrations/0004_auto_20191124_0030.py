# Generated by Django 2.2.7 on 2019-11-24 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_compatibilidade_computador_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vga',
            name='modelo',
            field=models.CharField(choices=[('gigabyte_geforce_gtx_1060_6gb', 'Gigabyte Geforce GTX 1060 6GB'), ('pny_rtx_2060_6gb', 'PNY RTX 2060 6GB'), ('radeon_rx_580_8GB', 'Radeon RX 580 8GB')], max_length=50, verbose_name='Modelo'),
        ),
    ]