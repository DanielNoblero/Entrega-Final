from django import forms
from AppRodriguezFinal.models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'