from django.urls import path
from AppCoder import views

#Los "name" son los nombres de los titulos del navbar

urlpatterns = [
    #Paths de la Navbar
    path('', views.inicio, name="Inicio"),
    path('alojamientos/',views.alojamientos, name="Alojamientos"),
    path('autos/', views.autos, name="Autos"),
    path('paquetes/', views.paquetes, name="Paquetes"),
    path('consultas/', views.consultas, name="Consultas"),
    path('sobre_mi/', views.sobre_mi, name="Sobre_mi"),
    path('inicio_logueado/', views.inicio_logueado, name="Inicio_logueado"),
    path('inicio_sesion/', views.inicio_sesion, name="Inicio_sesion"),
    #path('registro/', views.registro, name="Registro"),
    
    #Paths de busquedas
    path('alojamientos/buscar_alojamiento/',views.buscar_alojamiento),
    path('autos/buscar_auto/',views.buscar_auto),
    path('paquetes/buscar_paquete/',views.buscar_paquete),

    #Paths usuarios
    path('registro/',views.registro, name='Registro'),
    path('registro_correcto/',views.registro_correcto),
    path('registro_error/',views.registro_error),
    
    
    path('suscripcion/',views.suscripcion,name='Suscripcion'),
    path('paquete_confirmado/',views.paquete_confirmado, name='Paquete_confirmado'),
    

    #path('buscar_alojamiento/', views.buscar_alojamiento, name="Alojamientos"),
    #path('',views.busqueda_alojamientos, name="busqueda_alojamientos"),
    
    #path('rdo_busqueda_alojamientos/',views.rdo_busqueda_alojamientos,name='rdo_busqueda_alojamientos'),
]