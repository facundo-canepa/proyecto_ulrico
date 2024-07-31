from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    comision = models.CharField(max_length=100)

    def __str__(self):
        return f"Nombre del Curso: {self.nombre} - Numero de la Comisión: {self.comision}"
        
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100, blank=True)  # Corregido

    def __str__(self):
        return f"Nombre del Estudiante: {self.nombre} - Apellido del Estudiante : {self.apellido}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Nombre del Profesor: {self.nombre} - Apellido del Profesor : {self.apellido}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"Nombre del Entregable: {self.nombre} - Entregado : {self.entregado}"
