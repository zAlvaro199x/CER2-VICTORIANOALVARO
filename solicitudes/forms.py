# Municipalidad/solicitudes/forms.py

from django import forms
from .models import SolicitudDeRetiro, Material

class SolicitudDeRetiroForm(forms.ModelForm):
    class Meta:
        model = SolicitudDeRetiro
        fields = ['material', 'cantidad_estimada', 'fecha_retiro_estimada', 'direccion']
        widgets = {
            'fecha_retiro_estimada': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'material': forms.Select(attrs={'class': 'form-select'}),
            'cantidad_estimada': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu dirección de retiro'}),
        }
        labels = {
            'material': 'Tipo de Material',
            'cantidad_estimada': 'Cantidad Estimada (en kg)',
            'fecha_retiro_estimada': 'Fecha Estimada de Retiro',
            'direccion': 'Dirección de Retiro',
        }

    #Aplica estilos bootstrap genericos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['material', 'cantidad_estimada', 'fecha_retiro_estimada', 'direccion']:
                field.widget.attrs.update({'class': 'form-control'})