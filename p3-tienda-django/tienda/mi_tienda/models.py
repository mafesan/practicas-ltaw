from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=30)
    precio = models.FloatField()
    editorial = models.CharField(max_length=50)
    fecha_pub = models.DateField('Fecha de publicacion')
    def __unicode__(self):
        return self.autor + ", " + self.titulo


class Disco(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=30)
    precio = models.FloatField()
    discografica = models.CharField(max_length=50)
    fecha_pub = models.DateField('Fecha de publicacion')
    def __unicode__(self):
        return self.autor + ", " + self.titulo


class Bici(models.Model):
    modelo = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=400)
    def __unicode__(self):
        return self.marca + ", " + self.modelo
