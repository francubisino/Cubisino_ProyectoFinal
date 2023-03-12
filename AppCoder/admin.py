from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Alojamientos)
admin.site.register(Autos)
admin.site.register(Consultas)
admin.site.register(usuarios)
admin.site.register(Suscripciones)
admin.site.register(Profile)
admin.site.register(Comentario)

#class AlojamientoAdmin(admin.ModelAdmin):
#    readonly_fields = ('id',)
    
#admin.site.register(Alojamientos, AlojamientoAdmin)