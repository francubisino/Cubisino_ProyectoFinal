from django.db import models
from django.contrib.auth.models import User


class Autos(models.Model):
    marca=models.CharField(max_length=30)
    modelo=models.CharField(max_length=40)
    precio_dia=models.IntegerField()
    img_auto=models.ImageField(null=True, blank=True, upload_to='img/')
    
    def __str__(self):
        return '%s - %s' % (self.marca, self.modelo)

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
    propietario=models.CharField(max_length=30, default='Bote')
    
    def __unicode__(self,):
        return str(self.titulo)
    
   
class Consultas(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()    
    consulta=models.TextField(null=True,blank=True)

    def __str__(self):
            return '%s - %s' % (self.nombre, self.consulta)
        
class usuarios(models.Model):
    nombre=models.CharField(max_length=15)
    telefono=models.CharField(max_length=15)
    fecha_de_nacimiento=models.DateField()
    email=models.EmailField(max_length=245)
    username=models.CharField(max_length=245, default='NULL')
    password1=models.CharField(max_length=8, default='NULL')
    password2=models.CharField(max_length=8, default='NULL')
    
    def __str__(self):
        return '%s' % (self.username)
    
class Suscripciones(models.Model):
    email=models.EmailField()
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='img/',null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    link = models.URLField(max_length=200,null=True,blank=True)

    def __str__(self):
        return '%s' % (self.user)
    
class Comentario(models.Model):
    autor = models.CharField(max_length=20)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.CharField(max_length=20)
    titulo_alojamiento = models.CharField(max_length=20,default='NULL')

    def __str__(self):
        return '%s - %s' % (self.autor, self.mensaje)
    