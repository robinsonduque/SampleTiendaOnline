# Generated by Django 2.2.5 on 2022-09-25 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoWebTienda', '0003_auto_20220924_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='disponibilidad',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='tienda'),
        ),
        migrations.RemoveField(
            model_name='productos',
            name='categorias',
        ),
        migrations.AddField(
            model_name='productos',
            name='categorias',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ProyectoWebTienda.Categoria'),
        ),
    ]
