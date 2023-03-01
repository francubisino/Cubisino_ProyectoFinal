from django import forms
from AppCoder.models import usuarios
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse

class AutosFormulario(forms.Form):
    marca=forms.CharField(max_length=30)
    modelo=forms.CharField(max_length=40)
    precio_dia=forms.IntegerField()
    seguro=forms.BooleanField()

class ConsultasFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()    
    consulta=forms.CharField()

class AlojamientosFormulario(forms.Form):
    ubicacion=forms.CharField(max_length=30)
    precio_dia=forms.IntegerField()
    habitaciones=forms.IntegerField()
    tipo=forms.CharField(max_length=30)
    baños=forms.IntegerField()
    balcon=forms.BooleanField()
    pileta=forms.BooleanField()
    mascotas=forms.BooleanField()
    max_personas=forms.IntegerField()
    descripcion=forms.CharField(max_length=200)
    
class InicioFormulario(forms.Form):
    pais_origen=forms.CharField()
    
class PaquetesFormulario(forms.Form):
    paq_ubicacion=forms.CharField(max_length=30)
    paq_precio_aloja_dia=forms.IntegerField()
    paq_habitaciones=forms.IntegerField()
    paq_baños=forms.IntegerField()
    paq_balcon=forms.BooleanField()
    paq_pileta=forms.BooleanField()
    paq_mascotas=forms.BooleanField()
    paq_max_personas=forms.IntegerField()
    paq_interesa=forms.BooleanField()
    paq_marca=forms.CharField(max_length=30)
    paq_modelo=forms.CharField(max_length=40)
    paq_precio_auto_dia=forms.IntegerField()
    paq_seguro=forms.BooleanField()
    
class RegistrarUsuario(forms.Form):
    nombre = forms.CharField(label='Nombre:',max_length=15,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Nombre',
                                    }))
    telefono = forms.CharField(label='Teléfono',max_length=12,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'4421234567',
                                    }))
    fecha_de_nacimiento = forms.DateField(label='Fecha de nacimiento:',
                                    widget=forms.SelectDateWidget(years=range(1900,2001),
                                    attrs={
                                        'class':'form-control',
                                    }))
    email = forms.EmailField(label='Email:', max_length=245,
                             widget=forms.EmailInput(
                                 attrs={
                                     'class':'form-control',
                                     'placeholder':'ejemplo@ejemplo.com',
                                 }
                             ))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def registrar_usuario(self):
        password1=self.data['password1']
        password2=self.data['password2']
        
        if password1 != password2:
            int('contraseña erronea')  #Forzamos un error para que funcione el try/except del views.registro
        else:
            fecha = datetime(int(self.data['fecha_de_nacimiento_year']),
                            int(self.data['fecha_de_nacimiento_month']),
                            int(self.data['fecha_de_nacimiento_day']))
                
            nuevo_usuario = usuarios(nombre=self.data['nombre'],
                                    telefono=self.data['telefono'],
                                    fecha_de_nacimiento=fecha,
                                    email=self.data['email'],
                                    username=self.data['username'],
                                    password1=self.data['password1'],
                                    password2=self.data['password2'])
            nuevo_usuario.save()
            return 'Registro exitoso'