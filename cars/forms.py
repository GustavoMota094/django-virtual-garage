from django import forms
from .models import Car, MaintenanceRecord

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_type', 'year', 'trim_level', 'engine', 'nickname']

class MaintenanceRecordForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        fields = ['car', 'description', 'maintenance_type', 'date', 'parts_cost', 'labor_cost']
