# Generated by Django 2.2.5 on 2022-09-30 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallepedidos',
            old_name='pedido_id',
            new_name='pedido',
        ),
        migrations.RenameField(
            model_name='detallepedidos',
            old_name='producto_id',
            new_name='producto',
        ),
    ]