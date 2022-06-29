from datetime import datetime
from django import forms
from .models import ServicioMensajero




class ServicioMensajeroForm(forms.ModelForm):
    
    hora_recogida = forms.DateTimeField( initial=datetime.now)
    hora_entrega = forms.DateTimeField( initial=datetime.now)
    class Meta:
        model = ServicioMensajero
        fields='__all__'
  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)