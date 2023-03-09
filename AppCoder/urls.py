from django.urls import path
from AppCoder import views
from .views import ProfileUpdate

#Los "name" son los nombres de los titulos del navbar

urlpatterns = [
    #Paths de la Navbar
    path('', views.inicio, name="Inicio"),
    path('alojamientos/',views.alojamientos, name="Alojamientos"),
    path('autos/', views.autos, name="Autos"),
    path('mis_alojamientos/', views.mis_alojamientos, name="Mis_alojamientos"),
    path('paquetes/', views.paquetes, name="Paquetes"),
    path('consultas/', views.consultas, name="Consultas"),
    path('inicio/', views.suscripcion, name="Suscripciones"),
    path('sobre_mi/', views.sobre_mi, name="Sobre_mi"),
    path('inicio_logueado/', views.inicio_logueado, name="Inicio_logueado"),
    path('prueba/', views.pruebas, name="Pruebas"),
    path('cargar_alojamiento/', views.cargar_alojamiento, name="Cargar_alojamiento"),
    path('buscar_mis_alojamientos/', views.buscar_mis_alojamientos, name="Buscar_mis_alojamientos"),
    path('rdo_busqueda_mis_alojamientos/<titulo>/',views.borrarAlojamiento, name='Borrar_alojamiento'),
    path('inicio',views.borrarAlojamiento, name='Borrar_alojamiento'),
    
    #path('borrar_alojamiento/', views.borrarAlojamiento, name="Borrar_alojamiento"),
    #path('rdo_busqueda_mis_alojamientos/<titulo>/',views.borrarAlojamiento, name='Borrar_alojamiento'),
    
    
    
    
    #path('carga_alojamiento_correcta/', views.carga_alojamiento_correcta),
    #path(r'^upload$', 'upload_image_view', name='upload_image_view'),
    #path('accounts/login/', views.inicio_sesion, name="Inicio_sesion"),
    #path('logged_out/', views.logged_out, name="Cierre_sesion"),
    #path('registro/', views.registro, name="Registro"),
    
    #Paths de busquedas
    path('alojamientos/buscar_alojamiento/',views.buscar_alojamiento),
    path('autos/buscar_auto/',views.buscar_auto),
    path('paquetes/buscar_paquete/',views.buscar_paquete),
    path('mis_alojamientos/buscar_mis_alojamientos/', views.buscar_mis_alojamientos),

    #Paths usuarios
    path('registro/',views.registro, name='Registro'),
    path('registro_correcto/',views.registro_correcto),
    path('registro_error/',views.registro_error),
    path('profile/', ProfileUpdate.as_view(),name='profile'),
    #Login
    #Logout
    
    
    
    path('suscripcion/',views.suscripcion,name='Suscripcion'),
    path('reserva_confirmada/',views.reserva_confirmada, name='Reserva_confirmada'),
    

    #path('buscar_alojamiento/', views.buscar_alojamiento, name="Alojamientos"),
    #path('',views.busqueda_alojamientos, name="busqueda_alojamientos"),
    
    #path('rdo_busqueda_alojamientos/',views.rdo_busqueda_alojamientos,name='rdo_busqueda_alojamientos'),
]