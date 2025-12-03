from django.urls import path
from .views import GarageView, CarDetailView, CarCreateView, MaintenanceRecordView, AddMaintenanceRecordView
from .views import (
    GarageView,
    CarDetailView,
    CarCreateView,
    MaintenanceRecordView,
    AddMaintenanceRecordView,
    CarDeleteView
)

app_name = 'cars'

urlpatterns = [
    path('my-garage/', GarageView.as_view(), name='garage'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('add-car/', CarCreateView.as_view(), name='add_car'),
    path('maintenance_record/<int:pk>', MaintenanceRecordView.as_view(), name='maintenance_record'),
    path('add-maintenance_record/', AddMaintenanceRecordView.as_view(), name='add-maintenance_record'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='delete_car'),
]
