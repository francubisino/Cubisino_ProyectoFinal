from django import forms

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