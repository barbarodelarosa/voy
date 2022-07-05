"""voy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core import views
from django.urls import path


app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('cliente/', views.HomeClienteView.as_view(), name="home-cliente"),
    path('cliente/crear-mensajeria/', views.CrearServicioMensajeriaView.as_view(), name="crear-mensajeria"),
    path('cliente/crear-paquete/', views.CrearPaqueteView.as_view(), name="crear-paquete"),
    path('cliente/lista-de-paquetes/', views.ListaPaquetesView.as_view(), name="lista-paquetes"),
    path('cliente/seguimiento/', views.SeguimientoView.as_view(), name="seguimiento"),
    path('cliente/lista-servicio-mensajeria/', views.ListaServicioMensajeroView.as_view(), name="lista-servicio-mensajeria"),
    path('cliente/aceptar-mensajero/<pk>/<pk_mensajero>/', views.aceptar_mensajero, name="aceptar-mensajero"),
    path('cliente/rechazar-mensajero/<pk>/<pk_mensajero>/', views.rechazar_mensajero, name="rechazar-mensajero"),
    path('cliente/detalles-mensajero/<pk>/', views.DetallesMensajeroView.as_view(), name="detalles-mensajero"),
    path('cliente/seguimiento-mensajero/<pk>/', views.SeguimientoMensajeroView.as_view(), name="seguimiento-mensajero"),

    path('detalles-servicio-mensajero/<pk>/', views.DetallesServicioMensajeroView.as_view(), name="detalles-servicio-mensajero"),
    path('servicio-paquete-entregado-recibido/<pk_servicio>/<enviado_por>/', views.recogida_entrega_paquete, name="servicio-paquete-entregado-recibido"),

    path('mensajero/', views.HomeMensajeroView.as_view(), name="home-mensajero"),
    path('mensajero/mensajero-aceptar-servicio/<pk>/', views.mensajero_aceptar_servicio, name="mensajero-aceptar-servicio"),
    path('mensajero/rechazar-aceptar-servicio/<pk>/', views.rechazar_aceptar_servicio, name="rechazar-aceptar-servicio"),
    path('mensajero/detalles-cliente/<pk>/', views.DetallesClienteView.as_view(), name="detalles-cliente"),
    path('mensajero/detalles-paquete/<pk>/', views.DetallesPaqueteView.as_view(), name="detalles-paquete"),
    # path('mensajero/rechazar-mensajero/<pk>/<pk_mensajero>', views.rechazar_mensajero, name="rechazar-mensajero"),

]

