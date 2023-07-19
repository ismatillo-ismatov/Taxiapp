from rest_framework import serializers
from .models import Driver


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('trips', 'name', 'phone_number', 'car_number', 'car_model', 'patent', 'busy',
                  'create_at', 'update_at')

