from django.db import models
from app.models import *


# Create your models here.

class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    trips = models.OneToOneField('app.Trip', on_delete=models.CASCADE)
    name = models.CharField(max_length=110)
    phone_number = models.CharField(max_length=25)
    car_model = models.CharField(max_length=50)
    car_number = models.CharField(max_length=50)
    passport = models.CharField(max_length=50)
    patent = models.CharField(max_length=50)
    busy = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


