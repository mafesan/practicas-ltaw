# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_tienda', '0004_auto_20170408_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bici',
            name='imagen',
            field=models.ImageField(default=b'img/bike.png', max_length=150, upload_to=b'img'),
        ),
        migrations.AlterField(
            model_name='bici',
            name='video',
            field=models.FileField(default=b'vid/sample.mp4', max_length=150, upload_to=b'vid'),
        ),
        migrations.AlterField(
            model_name='disco',
            name='audio',
            field=models.FileField(default=b'aud/sample.mp3', max_length=150, upload_to=b'aud'),
        ),
        migrations.AlterField(
            model_name='disco',
            name='imagen',
            field=models.ImageField(default=b'img/music.png', max_length=150, upload_to=b'img'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(default=b'img/book.png', max_length=150, upload_to=b'img'),
        ),
    ]
