from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Pais(models.Model):
    pais_origen=models.CharField(max_length=40)
    idioma=models.CharField(max_length=40)

class Autos(models.Model):
    marca=models.CharField(max_length=30)
    modelo=models.CharField(max_length=40)
    precio_dia=models.IntegerField()
    img_auto=models.ImageField(null=True, blank=True, upload_to='img/')

class Alojamientos(models.Model):
    ubicacion=models.CharField(max_length=30, default='NULL')
    precio_dia=models.IntegerField(null=True, blank=True)
    habitaciones=models.IntegerField(default=0)
    tipo=models.CharField(max_length=30, default='NULL')
    baños=models.IntegerField(default=0)
    balcon=models.BooleanField(default=False)
    pileta=models.BooleanField(default=False)
    mascotas=models.BooleanField(null=False, blank=False,default=0)
    max_personas=models.IntegerField(default=0)
    titulo=models.CharField(max_length=100, default='NULL')
    img_alojamiento=models.ImageField(null=True, blank=True, upload_to='img/')
    descripcion=models.CharField(max_length=200, default='NULL')
    huesped=models.CharField(max_length=30, default='Desocupado')
    propietario=models.CharField(max_length=30, default='Bote')
    
    def __unicode__(self,):
        return str(self.img_alojamiento)
    
class Pruebas(models.Model):
    ubicacion=models.CharField(max_length=30)
    img_alojamiento=models.ImageField(upload_to='img/', null=True)



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

class usuarios(models.Model):
    nombre=models.CharField(max_length=15)
    telefono=models.CharField(max_length=15)
    fecha_de_nacimiento=models.DateField()
    email=models.EmailField(max_length=245)
    username=models.CharField(max_length=245, default='NULL')
    password1=models.CharField(max_length=8, default='NULL')
    password2=models.CharField(max_length=8, default='NULL')
    
class Suscripciones(models.Model):
    email=models.EmailField()
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='img/',null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    link = models.URLField(max_length=200,null=True,blank=True)



    
"""  https://www.youtube.com/watch?v=ketO-Pj35lo&list=PLGUsAPwPODljydJyw2ptMwoPdbpVzyjQe&index=18
class Comment(models.Model):
    content = models.TextField(max_length=1000, help_text='Ingrese un comentario')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        len_title = 15
        if len(self.content) > len_title:
            return self.content[:len_title] + '...'
        return self.content
"""
