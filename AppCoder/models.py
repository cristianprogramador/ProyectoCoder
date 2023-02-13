from django.db import models

# Create your models here.
# MODELOS BD
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nombre}: {str(self.camada)}'

class Estudiante(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.nombre} {str(self.apellido)}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Profesores'

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'
        

class Entregable(models.Model):

    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    