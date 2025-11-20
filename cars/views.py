from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Car, MaintenanceRecord
from .forms import CarForm, MaintenanceRecordForm

class GarageView(LoginRequiredMixin, ListView):
    """
    Displays a list of cars owned by the currently logged-in user.
    """
    model = Car
    template_name = 'cars/garage.html'
    context_object_name = 'user_cars'

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)
    
class CarDetailView(LoginRequiredMixin, DetailView):
    """
    Display details for a single car in the garage.
    """
    model = Car
    template_name = 'cars/car_detail.html'

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)
    
class CarCreateView(LoginRequiredMixin, CreateView):
    """
    Displays a form for adding a new car and handles form submission.
    """
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('cars:garage')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MaintenanceRecordView(LoginRequiredMixin, DetailView):
    """
    Display details for a single car in the garage.
    """
    model = MaintenanceRecord
    template_name = 'cars/maintenance_record.html'

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)
     
class AddMaintenanceRecordView(LoginRequiredMixin, CreateView):
    """
    Displays a form for adding a maitenance record for a car on the user's garage
    """
    model = MaintenanceRecord
    form_class = MaintenanceRecordForm
    template_name = 'cars/maintenance_record_form.html'
    success_url = reverse_lazy('cars:car_detail')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    