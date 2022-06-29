from django.contrib import admin
from .models import Cliente, Mensajero, ServicioMensajero
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Mensajero)
admin.site.register(ServicioMensajero)
