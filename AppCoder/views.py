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

def inicio_logueado(request):
    return render(request,'AppCoder/inicio_logueado.html')

def carga_alojamiento_correcta(request):
    return render(request,'AppCoder/carga_alojamiento_correcta.html')



def carga_alojamiento_correcta(request):
    return render(request,'AppCoder/carga_alojamiento_correcta.html')

#def inicio_sesion(request):
#    return render(request,'registration/login.html')

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
            #TIENE QUE SER UN AND, Y NO UN OR
            
            #alojamiento=Alojamientos.objects.filter(Q(habitaciones__icontains=habitaciones) | Q(ubicacion__icontains=ubicacion))
            
        return render(request,"AppCoder/rdo_busqueda_alojamientos.html", {"articulos":alojamiento, "query": ubicacion})
        
        
    #else:
        
        #mensaje='No ingresaste texto'
        #return render(request,"AppCoder/rdo_busqueda_alojamientos.html"mensaje)
        



#def rdo_busqueda_alojamientos(request):
#    return render(request, "AppCoder/inicio.html")


"""
def reservar_alojamiento(request):
    if request.method == 'POST':
        miFormulario = ReservarFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            consultas = Consultas(nombre=informacion['nombre'], 
                                  apellido=informacion['apellido'],
                                   email=informacion['email'],
                                    consulta=informacion['consulta'])
            consultas.save()
            return render(request,'AppCoder/inicio.html/')
    else:
        miFormulario = ConsultasFormulario()
        
    return render(request,'AppCoder/consultas.html', {"miFormulario":miFormulario})
    


def alojamientos(request):
    if request.method == 'POST':
        miFormulario = AlojamientosFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            alojamientos = Alojamientos(ubicacion=informacion['ubicacion'],
                                        precio_dia=informacion['precio_dia'],
                                        habitaciones=informacion['habitaciones'],
                                        baños=informacion['baños'],
                                        balcon=informacion['balcon'],
                                        pileta=informacion['pileta'],
                                        mascotas=informacion['mascotas'],
                                        max_personas=informacion['max_personas'])
            alojamientos.save()
            return render(request,'AppCoder/inicio.html/')
    else:
        miFormulario = AlojamientosFormulario()
        
    return render(request,'AppCoder/formularioInsert_alojamiento.html', {"miFormulario":miFormulario})
    
    #return render(request,'AppCoder/profesores.html')
"""
"""
def autos(request):
    if request.method == 'POST':
        miFormulario = AutosFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            autos = Autos(marca=informacion['marca'],
                                        modelo=informacion['modelo'],
                                        precio_dia=informacion['precio_dia'],
                                        seguro=informacion['seguro'])
            autos.save()
            return render(request,'AppCoder/inicio.html')
    else:
        miFormulario = AutosFormulario()
        
    return render(request,'AppCoder/formularioInsert_auto.html', {"miFormulario":miFormulario})
"""
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
                                        huesped="Desocupado",
                                        titulo= informacion['titulo'],
                                        img_alojamiento= informacion['img_alojamiento'])
           
            alojamiento.save()
            return render(request,'AppCoder/carga_alojamiento_correcta.html/')
   else:
        miFormulario = CargarAlojamientoFormulario()
        
   return render(request,'AppCoder/cargar_alojamiento.html', {"miFormulario":miFormulario})
    


def pruebas(request):
    if request.method == 'POST':
        miFormulario = PruebasFormulario(request.POST,request.FILES)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            prueba = Pruebas(ubicacion=informacion['ubicacion'],
                             img_alojamiento=informacion['img_alojamiento']
                             )
            prueba.save()
            return render(request,'AppCoder/consulta_enviada.html/')
    else:
        miFormulario = PruebasFormulario()
        
    return render(request,'AppCoder/prueba.html', {"miFormulario":miFormulario})



            
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
    
  
  
def paquetes(request):
    return render(request,'AppCoder/paquetes.html')

def reserva_confirmada(request):
    return render(request,'AppCoder/reserva_confirmada.html')

def buscar_paquete(request):
    if request.GET['paq_ubicacion']:
        paq_ubicacion=request.GET['paq_ubicacion']
        #modelo=request.GET['modelo']
        #precio_dia=request.GET['precio_dia']
        #seguro=request.GET['seguro']
                
        #articulos=Pais.objects.filter(pais_origen__icontains=producto)
        paquete=Paquetes.objects.filter(paq_ubicacion__icontains=paq_ubicacion)
        
        return render(request,"AppCoder/rdo_busqueda_paquetes.html", {"articulos":paquete, "query": paq_ubicacion})
        
        
    else:
        mensaje="No ingresaste texto"
    
    return HttpResponse(mensaje)


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


"""         max_personas=request.GET['max_personas']
            
        if request.GET['tipo'] == "Todos":
            tipo = ['Casa','Contenedores','Mansión','Casa-Quinta','Departamento']
        else:
            tipo = [request.GET['tipo']]
            
                alojamiento=Alojamientos.objects.filter(ubicacion__icontains=ubicacion,
                                                    precio_dia__lte=precio_dia, #Busca los que tienen precio_dia igual o menor al ingresado
                                                    habitaciones=habitaciones,
                                                    tipo__in=tipo,
                                                    baños__gte=baños,
                                                    balcon=balcon,
                                                    pileta=pileta,
                                                    mascotas=mascotas,
                                                    max_personas__gte=max_personas) 
            #TIENE QUE SER UN AND, Y NO UN OR
            
            #alojamiento=Alojamientos.objects.filter(Q(habitaciones__icontains=habitaciones) | Q(ubicacion__icontains=ubicacion))
            
        return render(request,"AppCoder/rdo_busqueda_alojamientos.html", {"articulos":alojamiento, "query": ubicacion})"""

#Views del CRUD
"""def leerProfesores(request):
    profesores= Profesor.objects.all()
    contexto = {"profesores": profesores}
    return render(request, "AppCoder/leerProfesores.html",contexto)
"""
"""
def borrarAlojamiento(request,titulo):
    alojamiento= Alojamientos.objects.get(titulo=titulo)
    if request.method == 'POST':
        miFormulario = AlojamientosFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            alojamiento.titulo=informacion['titulo'],
            
            alojamiento.save()
            return render(request,'AppCoder/rdo_busqueda_mis_alojamientos.html/') #Luego de ser ejecutado vuelve a esta pagina
    #else:
    #    miFormulario = ProfesorFormulario(initial = {'nombre': profesor.nombre,
    #                                                 'apellido': profesor.apellido,
    #                                                 'email': profesor.email,
    #                                                 'profesion': profesor.profesion})
    
    return render(request, "AppCoder/rdo_busqueda_mis_alojamientos.html", {"miFormulario":miFormulario})
"""
"""def eliminarProfesor(request,profesor_nombre):
    profesor= Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    
    profesores= Profesor.objects.all()
    contexto = {"profesores": profesores}
    return render(request, "AppCoder/leerProfesores.html",contexto)

def editarProfesor(request,profesor_nombre):
    profesor= Profesor.objects.get(nombre=profesor_nombre)
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            profesor.nombre=informacion['nombre'],
            profesor.apellido=informacion['apellido'],
            profesor.email=informacion['email'],
            profesor.profesion=informacion['profesion'],
            
            profesor.save()
            return render(request,'AppCoder/inicio.html/') #Luego de ser ejecutado vuelve a esta pagina
    else:
        miFormulario = ProfesorFormulario(initial = {'nombre': profesor.nombre,
                                                     'apellido': profesor.apellido,
                                                     'email': profesor.email,
                                                     'profesion': profesor.profesion})
    
    return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario})
"""

"""
class UserChangePassword(LoginRequiredMixin, FormView):
    model = User
    form_class= PasswordChangeForm
    template_name = 'AppCoder/change_password.html' 
    success_url= reverse_lazy('login')
"""
    
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