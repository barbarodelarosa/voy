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
from core.views import CrearPaqueteView, CrearServicioMensajeriaView, HomeClienteView, HomeView, ListaPaquetesView, ListaServicioMensajeroView, SeguimientoView
from django.urls import path


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('cliente/', HomeClienteView.as_view(), name="home-cliente"),
    path('cliente/crear-mensajeria/', CrearServicioMensajeriaView.as_view(), name="crear-mensajeria"),
    path('cliente/crear-paquete/', CrearPaqueteView.as_view(), name="crear-paquete"),
    path('cliente/lista-de-paquetes/', ListaPaquetesView.as_view(), name="lista-paquetes"),
    path('cliente/seguimiento/', SeguimientoView.as_view(), name="seguimiento"),
    path('cliente/lista-servicio-mensajeria/', ListaServicioMensajeroView.as_view(), name="lista-servicio-mensajeria"),
]

