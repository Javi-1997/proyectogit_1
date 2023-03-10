from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=64)
    comision = models.IntegerField()
    fecha_inicio = models.DateField(null=True)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return f"{self.nombre}, {self.comision}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=True)
    profesion = models.CharField(max_length=128)
    bio = models.TextField(null=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField()
    esta_aprobado = models.BooleanField(default=False)


class Instituto(models.Model):
    nombre = models.CharField(max_length=256)

class Entrada_de_blog(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=32)
    subtitulo = models.CharField(max_length=64)
    cuerpo = models.CharField(max_length=1000, null=True)
    fecha_publicacion = models.DateField(null=True)
    autor = models.CharField(max_length=64)
    imagen = models.ImageField(null=True, blank=True, upload_to='noticias')

    def __str__(self):
        return f"{self.titulo}"

class Avatar(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"

    