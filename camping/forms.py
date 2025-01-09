from django import forms
from .models import Campista, Reserva

class CampistaForm(forms.ModelForm):
    class Meta:
        model = Campista
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
