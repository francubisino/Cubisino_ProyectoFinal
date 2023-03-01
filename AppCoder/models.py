from django.db import models

# Create your models here.

class Pais(models.Model):
    pais_origen=models.CharField(max_length=40)
    idioma=models.CharField(max_length=40)

class Autos(models.Model):
    marca=models.CharField(max_length=30)
    modelo=models.CharField(max_length=40)
    precio_dia=models.IntegerField()
    seguro=models.BooleanField(default=False)

class Alojamientos(models.Model):
    ubicacion=models.CharField(max_length=30)
    precio_dia=models.IntegerField(null=True, blank=True)
    habitaciones=models.IntegerField()
    tipo=models.CharField(max_length=30)
    baños=models.IntegerField()
    balcon=models.BooleanField(default=False)
    pileta=models.BooleanField(default=False)
    mascotas=models.BooleanField(null=False, blank=False)
    max_personas=models.IntegerField()
    titulo=models.CharField(max_length=100)
    img_alojamiento=models.ImageField(null=True, blank=True, upload_to='img/')
    descripcion=models.CharField(max_length=200)

class Paquetes(models.Model):
    paq_ubicacion=models.CharField(max_length=30)
    paq_precio_aloja_dia=models.IntegerField()
    paq_habitaciones=models.IntegerField()
    paq_baños=models.IntegerField()
    paq_balcon=models.BooleanField(default=False)
    paq_pileta=models.BooleanField(default=False)
    paq_mascotas=models.BooleanField(default=False)
    paq_max_personas=models.IntegerField()
    paq_interesa=models.BooleanField()
    paq_marca=models.CharField(max_length=30)
    paq_modelo=models.CharField(max_length=40)
    paq_precio_auto_dia=models.IntegerField()
    paq_seguro=models.BooleanField(default=False)
    
class Consultas(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()    
    consulta=models.CharField(max_length=200)

