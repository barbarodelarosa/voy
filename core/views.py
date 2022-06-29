from django.http import HttpResponse
from core.forms import ServicioMensajeroForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Mensajero, Paquete, ServicioMensajero
# Create your views here.
class HomeView(generic.TemplateView):
    template_name="index.html"


class HomeClienteView(generic.View):
    template_name="cliente/index_cliente.html"

    def get(self, request, *args, **kwargs):
        # servicios=ServicioMensajero.objects.filter(user=self.request.user,activo=True)
        servicios=ServicioMensajero.objects.filter(activo=True)
        return render(request, self.template_name, {'servicios':servicios}) 


class CrearServicioMensajeriaView(generic.CreateView):
    form_class = ServicioMensajeroForm
    template_name="cliente/crear_mensajeria.html"
    success_url=reverse_lazy('core:home-cliente')




class CrearPaqueteView(generic.CreateView):
    model=Paquete
    fields=['user','mensajero','id']
    template_name="cliente/crear_paquete.html"
    success_url=reverse_lazy('core:lista-paquetes')

class ListaPaquetesView(generic.ListView):
    model=Paquete
    template_name="cliente/lista_de_paquetes.html"
    
class SeguimientoView(generic.TemplateView):
    template_name="cliente/seguimiento.html"
    
class ListaServicioMensajeroView(generic.ListView):
    model=ServicioMensajero
    template_name="cliente/lista_servicio_mensajeria.html"