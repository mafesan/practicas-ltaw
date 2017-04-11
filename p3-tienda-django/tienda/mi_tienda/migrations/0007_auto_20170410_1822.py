# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mi_tienda', '0006_carrito'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bicis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Tipo', models.CharField(max_length=10, null=True)),
                ('Marca', models.CharField(max_length=50, null=True)),
                ('Tamano', models.CharField(max_length=50, null=True)),
                ('Color', models.CharField(max_length=50, null=True)),
                ('Imagen', models.ImageField(null=True, upload_to=b'imagenes', blank=True)),
                ('Precio', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Discos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Tipo', models.CharField(max_length=10, null=True)),
                ('Grupo', models.CharField(max_length=50, null=True)),
                ('Disco', models.CharField(max_length=50, null=True)),
                ('Fecha', models.IntegerField(default=0, null=True)),
                ('Imagen', models.ImageField(null=True, upload_to=b'imagenes', blank=True)),
                ('Precio', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Tipo', models.CharField(max_length=10, null=True)),
                ('Autor', models.CharField(max_length=50, null=True)),
                ('Titulo', models.CharField(max_length=50, null=True)),
                ('Fecha', models.IntegerField(default=0, null=True)),
                ('Imagen', models.ImageField(null=True, upload_to=b'imagenes', blank=True)),
                ('Precio', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Tipo', models.CharField(max_length=50, null=True)),
                ('Prod_id', models.IntegerField(default=0, null=True)),
                ('Nombre', models.CharField(max_length=50, null=True)),
                ('Apellido', models.CharField(max_length=50, null=True)),
                ('Direccion', models.CharField(max_length=50, null=True)),
                ('Poblacion', models.CharField(max_length=50, null=True)),
                ('Precio', models.IntegerField(default=0, null=True)),
                ('Fecha', models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Bici',
        ),
        migrations.DeleteModel(
            name='Carrito',
        ),
        migrations.DeleteModel(
            name='Disco',
        ),
        migrations.DeleteModel(
            name='Libro',
        ),
    ]
