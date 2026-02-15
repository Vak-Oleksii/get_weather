from .models import Cities
from django.forms import ModelForm, TextInput

class CitiesForm(ModelForm):
    class Meta:
        model = Cities
        fields = ['name']
        widgets = {'name': TextInput(attrs={
                    'class': 'form-control',
                    'name': 'city',
                    'id': 'city',
                    'placeholder': 'City Name'})}