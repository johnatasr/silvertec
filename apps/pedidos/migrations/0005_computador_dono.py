# Generated by Django 2.2.7 on 2019-11-24 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_auto_20191124_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='computador',
            name='dono',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]