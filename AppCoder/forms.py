from django import forms
from AppCoder.models import usuarios, Alojamientos
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm

class AutosFormulario(forms.Form):
    marca=forms.CharField(max_length=30)
    modelo=forms.CharField(max_length=40)
    precio_dia=forms.IntegerField()
    seguro=forms.BooleanField()

class ConsultasFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()    
    consulta=forms.CharField(max_length=150)

class CargarAlojamientoFormulario(forms.Form):
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
    propietario=forms.CharField(max_length=30)
    titulo=forms.CharField(max_length=100)
    img_alojamiento=forms.ImageField()
   
class PruebasFormulario(forms.Form):
    ubicacion=forms.CharField(max_length=30)
    img_alojamiento=forms.ImageField()
    
class SuscripcionFormulario(forms.Form):
    email=forms.EmailField()    
    
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
    apellido = forms.CharField(label='Apellido:',max_length=15,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Apellido',
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
                     
            
            nuevo_usuario = User.objects.create_user(username=self.data['username'],
                                                    email=self.data['email'],
                                                    password=self.data['password1'],
                                                    first_name=self.data['nombre'],
                                                    last_name=self.data['apellido'],
                                                    is_staff=True)
            
            nuevo_usuario.save()
           
            return 'Registro exitoso'
        
"""       
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','bio','link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),  #el "clearable" es para que te de la opcion de borrarla
            'bio': forms.Textarea(attrs={'class':'form-control-file mt-3','rows':3,'placeholder':'Biografía'}),
            'avatar': forms.URLInput(attrs={'class':'form-control-file mt-3','placeholder':'Enlace'}),
        }
        #success_url = reverse_lazy('profile')
"""

class MisAlojamientosFormulario(forms.Form):
    propietario=forms.CharField(max_length=30)
    
    
class FormularioCambioPassword(PasswordChangeForm):
    old_password = forms.CharField(label=("Password Actual"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
