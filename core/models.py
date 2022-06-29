from core.utils import generate_ref_code
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Direccion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitud=models.DecimalField(max_digits=20, decimal_places=20, help_text="Latitud")
    longitud=models.DecimalField(max_digits=20, decimal_places=20, help_text="Longitud")
    direccion=models.CharField(max_length=125, help_text="Direccion completa")



class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para el cliente")
    nombres=models.CharField(max_length=50, blank=True, null=True)
    apellidos=models.CharField(max_length=75, blank=True, null=True)
    ci=models.CharField(max_length=11, blank=True, null=True, help_text="Numero de carnet de Identidad")
    telefono=models.CharField(max_length=11, blank=True, null=True, help_text="Numero de telefono")
    direcciones=models.ManyToManyField(Direccion, blank=True, help_text="Direcciones del cliente")
    # Agregar todos los campos para describir al cliente


class Mensajero(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para el mensajero")
    direcciones=models.ManyToManyField(Direccion, blank=True, help_text="Direcciones del mensajero")
    codigo = models.CharField(max_length=10, blank=True, unique=True)

    def save(self, *args, **kwargs):
	    if self.codigo=="":
		    codigo = generate_ref_code()
		    self.codigo = codigo
	    super().save(*args, **kwargs)
    # agregar entregas realizadas


    # Agregar todos los campos para describir al cliente

class VehiculoMensajero(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mensajero = models.ForeignKey(Mensajero, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para el vehiculo del mensajero")
    # chapa

    # Agregar todos los campos para describir al cliente


class Paquete(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mensajero = models.ForeignKey(Mensajero, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para el vehiculo del mensajero")
    codigo = models.CharField(max_length=10, blank=True, unique=True)

    def save(self, *args, **kwargs):
	    if self.codigo=="":
		    codigo = generate_ref_code()
		    self.codigo = codigo
	    super().save(*args, **kwargs)

    # Agregar todos los campos para describir al cliente


class ServicioMensajero(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para el vehiculo del mensajero")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    mensajero = models.ForeignKey(Mensajero, on_delete=models.CASCADE, blank=True, null=True)
    vahiculo = models.ForeignKey(VehiculoMensajero, on_delete=models.CASCADE, blank=True, null=True)
    direccion_origen=models.CharField(max_length=125, blank=True, null=True)
    direccion_destino=models.CharField(max_length=125, blank=True, null=True)
    direccion_origen_map=models.CharField(max_length=125, blank=True, null=True)
    direccion_destino_map=models.CharField(max_length=125, blank=True, null=True)
    latitud_origen=models.DecimalField(max_digits=25, decimal_places=20, help_text="Latitud Origen", blank=True, null=True)
    longitud_origen=models.DecimalField(max_digits=25, decimal_places=20, help_text="Longitud Origen", blank=True, null=True)
    latitud_destino=models.DecimalField(max_digits=25, decimal_places=20, help_text="Latitud Destino", blank=True, null=True)
    longitud_destino=models.DecimalField(max_digits=25, decimal_places=20, help_text="Longitud Destino", blank=True, null=True)
    distancia=models.DecimalField(max_digits=25, decimal_places=20, help_text="Longitud Destino", blank=True, null=True)
    tarifa=models.DecimalField(max_digits=25, decimal_places=20, help_text="Longitud Destino", blank=True, null=True)
    precio=models.DecimalField(max_digits=25, decimal_places=20, help_text="Longitud Destino", blank=True, null=True)
    hora_recogida=models.DateTimeField(verbose_name="Hora de recogida", blank=True, null=True)
    hora_entrega=models.DateTimeField(verbose_name="Hora de entrega", blank=True, null=True)
    activo=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    # PPONER EN UN ESTADO CUANDO SE CREA, EJEMPLO: EN ESPERA, ENVIANDO, TERMINADO
    estado=models.CharField(max_length=25, blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, unique=True)

    def save(self, *args, **kwargs):
	    if self.codigo=="":
		    codigo = generate_ref_code()
		    self.codigo = codigo
	    super().save(*args, **kwargs)
    
    # origen=models.C(Direccion, blank=True, help_text="Direccion de origen", on_delete=models.CASCADE, related_name="origen")
    # destino=models.ForeignKey(Direccion, blank=True, help_text="Direccion de destino", on_delete=models.CASCADE, related_name="destino")
    

    # Agregar todos los campos para describir estado del servicio, fecha de creado

class ValoracionServicioMensajero(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mensajero = models.ForeignKey(Mensajero, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vahiculo = models.ForeignKey(VehiculoMensajero, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para la valoracion del servicio de mensajero")

class ComentarioServicioMensajero(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mensajero = models.ForeignKey(Mensajero, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vahiculo = models.ForeignKey(VehiculoMensajero, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para el comentario del servicio de mensajero")


