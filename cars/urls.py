from django.urls import path
from .views import GarageView, CarDetailView, CarCreateView, MaintenanceRecordView, AddMaintenanceRecordView

app_name = 'cars'

urlpatterns = [
    path('my-garage/', GarageView.as_view(), name='garage'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('add-car/', CarCreateView.as_view(), name='add_car'),
    path('maintenance_record/<int:pk>', MaintenanceRecordView.as_view(), name='maintenance_record'),
    path('add-maintenance_record/', AddMaintenanceRecordView.as_view(), name='add_maintenance_record'),
]
