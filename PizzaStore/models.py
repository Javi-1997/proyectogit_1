from django.db import models

# Create your models here.

class Pizza(models.Model):
    cantidad = models.IntegerField(max_length=2)
    gusto = models.CharField(max_length=32)
    toppings = models.CharField(null=True)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return f"{self.gusto}, {self.a}"

class Empanadas(models.Model):
    cantidad = models.IntegerField(max_length=2)
    gusto = models.CharField(max_length=32)
    descripcion = models.TextField(null=True)

class Tartas(models.Model):
    cantidad = models.IntegerField(max_length=2)
    gusto = models.CharField(max_length=32)
    descripcion = models.TextField(null=True)