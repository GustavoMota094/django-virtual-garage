from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_type', 'year', 'trim_level', 'engine', 'nickname']
