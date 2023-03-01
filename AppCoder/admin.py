from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Alojamientos)
admin.site.register(Autos)
admin.site.register(Paquetes)
admin.site.register(Consultas)

#class AlojamientoAdmin(admin.ModelAdmin):
#    readonly_fields = ('id',)
    
#admin.site.register(Alojamientos, AlojamientoAdmin)