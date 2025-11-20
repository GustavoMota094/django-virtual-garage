from django.urls import path
from .views import GarageView, CarDetailView, CarCreateView

app_name = 'cars'

urlpatterns = [
    path('my-garage/', GarageView.as_view(), name='garage'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('add-car/', CarCreateView.as_view(), name='add_car'),
]
