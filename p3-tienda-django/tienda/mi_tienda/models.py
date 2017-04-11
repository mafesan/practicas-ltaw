from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    editorial = models.CharField(max_length=50)
    fecha_pub = models.DateField('Fecha de publicacion')
    imagen = models.ImageField(upload_to='img',max_length=150, default='img/book.png')
    cantidad = models.IntegerField(default=0)
    def __unicode__(self):
        return self.autor + ", " + self.titulo


class Disco(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    discografica = models.CharField(max_length=50)
    fecha_pub = models.DateField('Fecha de publicacion')
    imagen = models.ImageField(upload_to='img',max_length=150, default='img/music.png')
    cantidad = models.IntegerField(default=0)
    audio = models.FileField(upload_to='aud',max_length=150, default='aud/sample.mp3')
    def __unicode__(self):
        return self.autor + ", " + self.titulo


class Bici(models.Model):
    modelo = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    pulgadas_rueda = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    descripcion = models.CharField(max_length=400)
    imagen = models.ImageField(upload_to='img',max_length=150, default='img/bike.png')
    video = models.FileField(upload_to='vid',max_length=150, default='vid/sample.mp4')
    cantidad = models.IntegerField(default=0)
    def __unicode__(self):
        return self.marca + ", " + self.modelo + " " + str(self.pulgadas_rueda)


class Carrito(models.Model):
    tipo_producto = models.CharField(max_length=200)
    campo1 = models.CharField(max_length=200)
    campo2 = models.CharField(max_length=200)
    def __unicode__(self):
        return self.tipo_producto + ": " + self.campo1 + " " + str(self.campo2)
