# Generated by Django 2.2.7 on 2019-11-24 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0009_auto_20191124_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processador',
            name='marca',
        ),
    ]
