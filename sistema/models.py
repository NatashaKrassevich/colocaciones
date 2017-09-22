from django.db import models
# Create your models here.
from django.utils import timezone

class Agencia(models.Model):
    telefono = models.CharField(max_length=200) 
    direccion = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)   
   
class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=200)
    fechaNac = models.EmailField(max_length=200)
    tipoDeTrabajo = models.ForeignKey('TipoDeTrabajo')
    activo = models.BooleanField()
    sexo = models.CharField(max_length=9)

    def __str__(self):
        return self.nombre


class Empresa(models.Model):
    nombreDeEmpresa = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    direccion = models.CharField(max_lenght=200)
    email = models.EmailField(max_lenght=100)
    cuit = models.CharField(max_lenght=200)

    def __str__(self):
        return self.nombreDeEmpresa


class RegistroDeEmpleados(models.Model):
    desocupado = models.ForeignKey('Persona')
    empresa = models.Foreignkey('Empresa')
    fechaDeContratacion = models.DateTimeField()
    fechaDeBaja = models.DateTimeField()

    def __str__(self):
        return self.desocupado


class OfertaDeTrabajo(models.Model):
    empresa = models.ForeignKey('Empresa')
    informacionNecesaria = models.CharField(max_lenght=200)
    fecha = models.DateTimeField()
    activas =  models.BooleanField()
    tipoDeTrabajo = ForeignKey('TipoDeTrabajo')


class TipoDeTrabajo(models.Model):
    tipoDeTrabajo = models.CharField(max_length=200)

    def __str__(self):
        return self.tipoDeTrabajo
