# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_tienda', '0005_auto_20170408_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_producto', models.CharField(max_length=200)),
                ('campo1', models.CharField(max_length=200)),
                ('campo2', models.CharField(max_length=200)),
            ],
        ),
    ]
