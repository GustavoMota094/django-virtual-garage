from django.db import models
from django.contrib.auth.models import User # Import the User model

class CarType(models.Model):
    """
    Represents a specific make and model of a car, e.g., "Ford Mustang".
    This will be our pre-defined list.
    """
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.make} {self.model}"

class Car(models.Model):
    """
    Represents a single car in a user's garage.
    """
    car_type = models.ForeignKey(CarType, on_delete=models.PROTECT)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    trim_level = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)

    year = models.PositiveIntegerField()
    nickname = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.year} {self.car_type.make} {self.car_type.model} ({self.owner.username})"

class MaintenanceRecord(models.Model):
    """
    Represents a single maintenance record for a car.
    """
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='maintenance_logs')
    description = models.TextField()
    maintenance_type = models.BooleanField()
    date = models.DateField()
    parts_cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    labor_cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Log for {self.car} on {self.date}"
    