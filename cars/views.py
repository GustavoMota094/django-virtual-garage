from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Car
from .forms import CarForm

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
        """
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        We override it to set the owner of the car to the current user.
        """
        form.instance.owner = self.request.user
        return super().form_valid(form)
    