# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_tienda', '0007_auto_20170410_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bici',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modelo', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=20)),
                ('pulgadas_rueda', models.IntegerField(default=0)),
                ('precio', models.DecimalField(max_digits=7, decimal_places=2)),
                ('descripcion', models.CharField(max_length=400)),
                ('imagen', models.ImageField(default=b'img/bike.png', max_length=150, upload_to=b'img')),
                ('video', models.FileField(default=b'vid/sample.mp4', max_length=150, upload_to=b'vid')),
                ('cantidad', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_producto', models.CharField(max_length=200)),
                ('campo1', models.CharField(max_length=200)),
                ('campo2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Disco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=30)),
                ('precio', models.DecimalField(max_digits=5, decimal_places=2)),
                ('discografica', models.CharField(max_length=50)),
                ('fecha_pub', models.DateField(verbose_name=b'Fecha de publicacion')),
                ('imagen', models.ImageField(default=b'img/music.png', max_length=150, upload_to=b'img')),
                ('cantidad', models.IntegerField(default=0)),
                ('audio', models.FileField(default=b'aud/sample.mp3', max_length=150, upload_to=b'aud')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=30)),
                ('precio', models.DecimalField(max_digits=5, decimal_places=2)),
                ('editorial', models.CharField(max_length=50)),
                ('fecha_pub', models.DateField(verbose_name=b'Fecha de publicacion')),
                ('imagen', models.ImageField(default=b'img/book.png', max_length=150, upload_to=b'img')),
                ('cantidad', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Bicis',
        ),
        migrations.DeleteModel(
            name='Discos',
        ),
        migrations.DeleteModel(
            name='Libros',
        ),
        migrations.DeleteModel(
            name='Pedidos',
        ),
    ]
