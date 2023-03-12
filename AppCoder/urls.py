from django.urls import path
from AppCoder import views
from .views import ProfileUpdate, MyPasswordChangeView, MyPasswordResetDoneView,CambioPassword

#Los "name" son los nombres de los titulos del navbar

urlpatterns = [
    #Paths de la Navbar
    path('', views.inicio, name="Inicio"),
    path('alojamientos/',views.alojamientos, name="Alojamientos"),
    path('autos/', views.autos, name="Autos"),
    path('paquetes/', views.paquetes, name="Paquetes"),
    path('mis_alojamientos/', views.mis_alojamientos, name="Mis_alojamientos"),
    path('consultas/', views.consultas, name="Consultas"),
    path('inicio/', views.suscripcion, name="Suscripciones"),
    path('sobre_mi/', views.sobre_mi, name="Sobre_mi"),
 
    #Paths funcionalidades
    path('cargar_alojamiento/', views.cargar_alojamiento, name="Cargar_alojamiento"),
    path('buscar_mis_alojamientos/', views.buscar_mis_alojamientos, name="Buscar_mis_alojamientos"),
    path('rdo_busqueda_mis_alojamientos/<titulo>/',views.borrarAlojamiento, name='Borrar_alojamiento'),
    path('editar_alojamiento/<int:pk>',views.editar_alojamiento, name='Editar_alojamiento'),
    path('inicio',views.borrarAlojamiento, name='Borrar_alojamiento'),
    path('alojamientos/buscar_alojamiento/',views.buscar_alojamiento),
    path('autos/buscar_auto/',views.buscar_auto),
    path('mis_alojamientos/buscar_mis_alojamientos/', views.buscar_mis_alojamientos),
     path('reserva_confirmada/',views.reserva_confirmada, name='Reserva_confirmada'),

    #Paths de comentarios
    path('comentarios/',views.ver_comentarios, name='comentarios'),
    path('agregar_comentario/comentarios/',views.agregar_comentario, name='agregar_comentario'),

    #Paths usuarios
    path('registro/',views.registro, name='Registro'),
    path('registro_correcto/',views.registro_correcto),
    path('registro_error/',views.registro_error),
    path('profile/', ProfileUpdate.as_view(),name='profile'),
    path('cambio_password/', CambioPassword.as_view(), name='cambiar_password'),
    path('cambio_pw_correcto/' , views.password_exitoso, name='password_exitoso'),
    path('suscripcion/',views.suscripcion,name='Suscripcion'),
    

]