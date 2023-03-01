from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.db.models import Q
# Create your views here.

def inicio(request):
    return render(request,'AppCoder/inicio.html')

def inicio_logueado(request):
    return render(request,'AppCoder/inicio_logueado.html')

def inicio_sesion(request):
    return render(request,'AppCoder/inicio_sesion.html')

def registro(request):
    return render(request,'AppCoder/registro.html')

def alojamientos(request):
    return render(request,'AppCoder/alojamientos.html')

def sobre_mi(request):
    return render(request,'AppCoder/sobre_mi.html')

def buscar_alojamiento(request):
    ######HACERLO DE ESTA FORMA!!!!!!!! GENIOOOOOO!!!!!!!
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
            return render(request,'AppCoder/inicio.html/')
    else:
        miFormulario = ConsultasFormulario()
        
    return render(request,'AppCoder/consultas.html', {"miFormulario":miFormulario})
    
    #return render(request,'AppCoder/estudiantes.html')
  
  
def paquetes(request):
    return render(request,'AppCoder/paquetes.html')

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
    if request.GET['marca']:
        marca=request.GET['marca']
        #modelo=request.GET['modelo']
        #precio_dia=request.GET['precio_dia']
        #seguro=request.GET['seguro']
                
        #articulos=Pais.objects.filter(pais_origen__icontains=producto)
        auto=Autos.objects.filter(marca__icontains=marca)
        
        return render(request,"AppCoder/rdo_busqueda_autos.html", {"articulos":auto, "query": marca})
        
        
    else:
        mensaje="No ingresaste texto"
    
    return HttpResponse(mensaje)


#def rdo_busqueda_alojamientos(request):
#    return render(request, "AppCoder/inicio.html")

