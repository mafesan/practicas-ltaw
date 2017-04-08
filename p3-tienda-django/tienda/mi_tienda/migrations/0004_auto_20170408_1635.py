# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_tienda', '0003_auto_20170327_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='bici',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bici',
            name='imagen',
            field=models.ImageField(default=b'path/to/my/default/image.jpg', max_length=150, upload_to=b'img'),
        ),
        migrations.AddField(
            model_name='bici',
            name='video',
            field=models.FileField(default=b'path/to/my/default/image.jpg', max_length=150, upload_to=b'vid'),
        ),
        migrations.AddField(
            model_name='disco',
            name='audio',
            field=models.FileField(default=b'path/to/my/default/sample.mp3', max_length=150, upload_to=b'aud'),
        ),
        migrations.AddField(
            model_name='disco',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='disco',
            name='imagen',
            field=models.ImageField(default=b'path/to/my/default/image.jpg', max_length=150, upload_to=b'img'),
        ),
        migrations.AddField(
            model_name='libro',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(default=b'path/to/my/default/image.jpg', max_length=150, upload_to=b'img'),
        ),
        migrations.AlterField(
            model_name='bici',
            name='precio',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='disco',
            name='precio',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='libro',
            name='precio',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
    ]
