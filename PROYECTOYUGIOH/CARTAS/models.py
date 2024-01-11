from django.db import models

# Create your models here.


class Serie(models.Model):

    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    invocacion = models.CharField(max_length=40)
    personajes = models.CharField(max_length=40)

class Juego(models.Model):

    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    invocacion = models.CharField(max_length=40)
    personajes = models.CharField(max_length=40)


class Pelicula(models.Model):

    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    invocacion = models.CharField(max_length=40)
    personajes = models.CharField(max_length=40)