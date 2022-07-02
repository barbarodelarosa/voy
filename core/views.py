from django.http import HttpResponse, HttpResponseRedirect
from core.forms import ServicioMensajeroForm
from django.shortcuts import redirect, render
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


class HomeMensajeroView(generic.View):
    template_name="mensajero/index_mensajero.html"

    def get(self, request, *args, **kwargs):
        # servicios=ServicioMensajero.objects.filter(user=self.request.user,activo=True)
        servicios=ServicioMensajero.objects.filter(activo=True)
        return render(request, self.template_name, {'servicios':servicios}) 

def mensajero_aceptar_servicio(request, pk):
    servicio = ServicioMensajero.objects.get(pk=pk)
    mensajero = request.user.mensajero
    print(servicio.mensajero)
    if not servicio.mensajero:
        servicio.mensajero = mensajero
        servicio.save()
    else:
        print("Ya existe un mensajero")
    
    # agregar logica para cambiar el estado del pedido que no es confirmado hasta que no esprobado por el creador
    url_actual= request.META.get('HTTP_REFERER', None) or '/'
    return redirect(url_actual)

def rechazar_aceptar_servicio(request, pk):
    servicio = ServicioMensajero.objects.get(pk=pk)
    mensajero = request.user.mensajero
    if not servicio.rechazo_mensajero.contains(mensajero):
        servicio.rechazo_mensajero.add(mensajero)
        servicio.save()
        print("Mensajero agregado")
    else:
        servicio.rechazo_mensajero.remove(mensajero)
        servicio.save()
        print("Mensajero removido")
    
    # agregar logica para cambiar el estado del pedido que no es confirmado hasta que no esprobado por el creador
    url_actual= request.META.get('HTTP_REFERER', None) or '/'
    return redirect(url_actual)

def aceptar_mensajero(request, pk, pk_mensajero):
    servicio = ServicioMensajero.objects.get(pk=pk)
    mensajero = Mensajero.objects.get(pk=pk_mensajero)
  
    print(servicio.mensajero)    
    if servicio.mensajero == mensajero:
        servicio.mensajero_aceptado=True
        servicio.estado = 'ENVIANDO'
        servicio.save()        
    else:
        print("No existem mensajero asignado")
    # agregar logica para cambiar el estado del pedido que no es confirmado hasta que no esprobado por el creador
    url_actual= request.META.get('HTTP_REFERER', None) or '/'
    return redirect(url_actual)

def rechazar_mensajero(request, pk, pk_mensajero):
    servicio = ServicioMensajero.objects.get(pk=pk)
    mensajero = Mensajero.objects.get(pk=pk_mensajero)
        
    if servicio.mensajero == mensajero:
        servicio.mensajero = None
        servicio.mensajero_rechazado.add(mensajero)
        servicio.estado = 'PENDIENTE_DE_MENSAJERO'
        servicio.save()        
    else:
        print("No existem mensajero asignado")
    # agregar logica para cambiar el estado del pedido que no es confirmado hasta que no esprobado por el creador
    url_actual= request.META.get('HTTP_REFERER', None) or '/'
    return redirect(url_actual)