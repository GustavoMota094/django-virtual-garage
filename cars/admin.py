from django.contrib import admin
from .models import Car, CarType, MaintenanceLog

admin.site.register(Car)
admin.site.register(CarType)
admin.site.register(MaintenanceLog)
