# Generated by Django 2.2.7 on 2019-11-24 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_computador_dono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placamae',
            name='processador_socket',
        ),
    ]
