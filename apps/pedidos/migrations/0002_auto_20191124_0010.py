# Generated by Django 2.2.7 on 2019-11-24 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processador',
            name='marca',
            field=models.CharField(choices=[('amd', 'AMD'), ('intel', 'Intel')], max_length=20, verbose_name='Marca'),
        ),
    ]
