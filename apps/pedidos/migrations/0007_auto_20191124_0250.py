# Generated by Django 2.2.7 on 2019-11-24 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0006_remove_placamae_processador_socket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computador',
            name='dono',
        ),
        migrations.AddField(
            model_name='computador',
            name='descricao',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
