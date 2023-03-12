from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.db.models import Q
from django import forms
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import views
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Profile
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView
from django.contrib.auth.forms import PasswordChangeForm
from .forms import  FormularioCambioPassword


# Create your views here.


def inicio(request):
    return render(request,'AppCoder/inicio.html')

def paquetes(request):
    return render(request,'AppCoder/paquetes.html')

def carga_alojamiento_correcta(request):
    return render(request,'AppCoder/carga_alojamiento_correcta.html')

def registro(request):
    mis_usuarios= User.objects.all()
    if request.method == 'POST':
       register_form = RegistrarUsuario(request.POST)
       if register_form.is_valid():
           try:
                success = register_form.registrar_usuario()
           except:
                return render(request, 'AppCoder/registro_error.html')        
           return render(request, 'AppCoder/registro_correcto.html')
    else:
            #Muestra nuestro form
        register_form = RegistrarUsuario()
        return render(request, 'AppCoder/registro.html',
                        {'register_form': register_form,
                        'usuarios': mis_usuarios})
 
def registro_correcto(request):
    return render(request,'AppCoder/registro_correcto.html')

def registro_error(request):
    return render(request,'AppCoder/registro_error.html')

def alojamientos(request):
    return render(request,'AppCoder/alojamientos.html')

def mis_alojamientos(request):
    return render(request,'AppCoder/mis_alojamientos.html')

def comentarios(request):
    return render(request,'AppCoder/comentarios.html')

def sobre_mi(request):
    return render(request,'AppCoder/sobre_mi.html')

def buscar_alojamiento(request):
    if request.GET['ubicacion'] and request.GET['max_personas'] and request.GET['habitaciones']:
        ubicacion=request.GET['ubicacion']
        habitaciones=request.GET['habitaciones']
        max_personas=request.GET['max_personas']
        
        
        if request.GET['tipo'] == "Todos":
            tipo = ['Casa','Contenedores','Mansión','Casa-Quinta','Departamento']
        else:
            tipo = [request.GET['tipo']]
        if request.GET['mascotas'] == "No":
            mascotas=False
        elif request.GET['mascotas'] == "Sí":
            mascotas=True
        if request.GET['balcon'] == "No":
            balcon=False
        elif request.GET['balcon'] == "Sí":
            balcon=True
        if request.GET['pileta'] == "No":
            pileta=False
        elif request.GET['pileta'] == "Sí":
            pileta=True
        if request.GET['precio_dia']:
            precio_dia=request.GET['precio_dia']
        else:
            precio_dia=99999999999
        if request.GET['baños']:
            baños=request.GET['baños']
        else:
            baños=1
        
    
    
        alojamiento=Alojamientos.objects.filter(ubicacion__icontains=ubicacion,
                                                    precio_dia__lte=precio_dia, #Busca los que tienen precio_dia igual o menor al ingresado
                                                    habitaciones=habitaciones,
                                                    tipo__in=tipo,
                                                    baños__gte=baños,
                                                    balcon=balcon,
                                                    pileta=pileta,
                                                    mascotas=mascotas,
                                                    max_personas__gte=max_personas) 

            
        return render(request,"AppCoder/rdo_busqueda_alojamientos.html", {"articulos":alojamiento, "query": ubicacion})
        
        
def consultas(request):
    if request.method == 'POST':
        miFormulario = ConsultasFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            consultas = Consultas(nombre=informacion['nombre'], 
                                  apellido=informacion['apellido'],
                                   email=informacion['email'],
                                    consulta=informacion['consulta'])
            consultas.save()
            return render(request,'AppCoder/consulta_enviada.html/')
    else:
        miFormulario = ConsultasFormulario()
        
    return render(request,'AppCoder/consultas.html', {"miFormulario":miFormulario})

def cargar_alojamiento(request):
   if request.method == 'POST':
        miFormulario = CargarAlojamientoFormulario(request.POST,request.FILES)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            alojamiento = Alojamientos(ubicacion=informacion['ubicacion'],
                                       precio_dia=informacion['precio_dia'],
                                        habitaciones= informacion['habitaciones'],
                                        tipo= informacion['tipo'],
                                        baños= informacion['baños'],
                                        balcon= informacion['balcon'],
                                        pileta= informacion['pileta'],
                                        mascotas= informacion['mascotas'],
                                        max_personas= informacion['max_personas'],
                                        descripcion= informacion['descripcion'],
                                        propietario=informacion['propietario'],
                                        titulo= informacion['titulo'],
                                        img_alojamiento= informacion['img_alojamiento'])
           
            alojamiento.save()
            return render(request,'AppCoder/carga_alojamiento_correcta.html/')
   else:
        miFormulario = CargarAlojamientoFormulario()
        
   return render(request,'AppCoder/cargar_alojamiento.html', {"miFormulario":miFormulario})
    
            
def suscripcion(request):
    if request.method == 'POST':
        miFormulario = SuscripcionFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            suscripcion = Suscripciones(email=informacion['email'])
            
            suscripcion.save()
            return render(request,'AppCoder/suscripcion_correcta.html/')
    else:
        miFormulario = SuscripcionFormulario()
        
    return render(request,'AppCoder/inicio.html', {"miFormulario":miFormulario})
    

def reserva_confirmada(request):
    return render(request,'AppCoder/reserva_confirmada.html')


def autos(request):
    return render(request,'AppCoder/autos.html')

def buscar_auto(request):
    if request.GET['marca'] == "Todos":
        marca = ['Ford','Citroen','Chevrolet','Volkswagen']
    else:
        marca = [request.GET['marca']]
    
    if request.GET['precio_dia']:
        precio_dia=request.GET['precio_dia']
    else:
        precio_dia=99999999999
      
    if request.GET['modelo']:
        modelo=request.GET['modelo']
           
        auto=Autos.objects.filter((Q(marca__icontains=marca)|Q(marca__in=marca)),
                                    modelo__icontains=modelo,
                                    precio_dia__lte=precio_dia)
    else:
        auto=Autos.objects.filter((Q(marca__icontains=marca)|Q(marca__in=marca)),
                                    precio_dia__lte=precio_dia)
        
    return render(request,"AppCoder/rdo_busqueda_autos.html", {"articulos":auto, "query": marca})

def buscar_mis_alojamientos(request):
    global propietario,propietarios
    propietario = [request.GET['propietario']]
              
    propietarios=Alojamientos.objects.filter(propietario__in=propietario)
    
        
    return render(request,"AppCoder/rdo_busqueda_mis_alojamientos.html", {"articulos":propietarios, "query": propietario})
    #return render(request,"AppCoder/rdo_busqueda_mis_alojamientos.html")


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    #form_class=ProfileForm
    model = Profile
    fields = ['avatar','bio','link']
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        try:
            return Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            return Profile.objects.create(user=self.request.user)
        #profile, created = Profile.objects.get_or_create(user=self.request.user)
        #return profile
       # return Profile.objects.get(user=self.request.user)
       

def borrarAlojamiento(request,titulo):
    alojamiento= get_object_or_404(Alojamientos, titulo=titulo)
    alojamiento.delete()


           
    propietarios=Alojamientos.objects.filter(propietario__in=propietario)
           
    return render(request,"AppCoder/rdo_busqueda_mis_alojamientos.html", {"articulos":propietarios, "query": propietario})

   
class MyPasswordChangeView(PasswordChangeView):
    template_name='AppCoder/change_password.html'
    success_url=reverse_lazy('password-change-done')

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name='AppCoder/change_password_done.html'


class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'AppCoder/cambio_password.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'AppCoder/cambio_pw_correcto.html', {})


def ver_comentarios(request):
    
    titulo_alojamiento=request.GET['titulo']
    
    alojamiento=Comentario.objects.filter(titulo_alojamiento=titulo_alojamiento)
    
        
    return render(request,"AppCoder/comentarios.html", {"comentarios":alojamiento, "query": titulo_alojamiento})

def agregar_comentario(request):
   
    if request.method == 'POST':
        miFormulario = ComentarioFormulario(request.POST)
        print(miFormulario)
       
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            comentario = Comentario(autor=informacion['autor'],
                                    mensaje=informacion['mensaje'],
                                    fechaComentario=informacion['fecha_comentario'],
                                    titulo_alojamiento=informacion['titulo_alojamiento'])
            comentario.save()
            return render(request,'AppCoder/comentario_enviado.html/')
    else:
        miFormulario = ComentarioFormulario()
        
    return render(request,'AppCoder/comentarios.html', {"miFormulario":miFormulario})


def editar_alojamiento(request,pk):
    
   alojamiento= get_object_or_404(Alojamientos, id=pk)

   form= CargarAlojamientoFormulario(initial={'ubicacion':alojamiento.ubicacion,
                                              'precio_dia':alojamiento.precio_dia,
                                              'habitaciones':alojamiento.habitaciones,
                                              'tipo':alojamiento.tipo,
                                              'baños':alojamiento.baños,
                                              'balcon':alojamiento.balcon,
                                              'pileta':alojamiento.pileta,
                                              'mascotas':alojamiento.mascotas,
                                              'max_personas':alojamiento.max_personas,
                                              'descripcion':alojamiento.descripcion,
                                              'propietario':alojamiento.propietario,
                                              'titulo':alojamiento.titulo,
                                              'img_alojamiento':alojamiento.img_alojamiento
                                                })
   if request.method == 'POST':
        form = CargarAlojamientoFormulario(request.POST,request.FILES)
        
        
        if form.is_valid():
            
                       
            alojamiento.ubicacion=form.cleaned_data['ubicacion']
            alojamiento.precio_dia=form.cleaned_data['precio_dia']
            alojamiento.habitaciones=form.cleaned_data['habitaciones']
            alojamiento.tipo=form.cleaned_data['tipo']
            alojamiento.baños=form.cleaned_data['baños']
            alojamiento.balcon=form.cleaned_data['balcon']
            alojamiento.pileta=form.cleaned_data['pileta']
            alojamiento.mascotas=form.cleaned_data['mascotas']
            alojamiento.max_personas=form.cleaned_data['max_personas']
            alojamiento.descripcion=form.cleaned_data['descripcion']
            alojamiento.propietario=form.cleaned_data['propietario']
            alojamiento.titulo=form.cleaned_data['titulo']
            alojamiento.img_alojamiento=form.cleaned_data['img_alojamiento']
           
            alojamiento.save()
            return render(request,'AppCoder/edicion_alojamiento_correcta.html/')
   else:
        print('invalido')
   return render(request,'AppCoder/editar_alojamiento.html', {"form":form})
