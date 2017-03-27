# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bici',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modelo', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Disco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('discografica', models.CharField(max_length=50)),
                ('fecha_pub', models.DateTimeField(verbose_name=b'Fecha de publicacion')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('editorial', models.CharField(max_length=50)),
                ('fecha_pub', models.DateTimeField(verbose_name=b'Fecha de publicacion')),
            ],
        ),
    ]
