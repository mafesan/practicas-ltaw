# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disco',
            name='fecha_pub',
            field=models.DateField(verbose_name=b'Fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='fecha_pub',
            field=models.DateField(verbose_name=b'Fecha de publicacion'),
        ),
    ]
