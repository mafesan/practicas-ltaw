# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_tienda', '0002_auto_20170327_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='bici',
            name='pulgadas_rueda',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bici',
            name='precio',
            field=models.FloatField(),
        ),
    ]
