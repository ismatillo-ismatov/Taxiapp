from django.shortcuts import render
from rest_framework import generics
from .models import Driver
from .serializers import DriverSerializer


class DriverListAPIView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class DriverRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_field = 'id'


class DriverCreateAPIView(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class DriverUpdateAPIView(generics.UpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_field = 'id'


class DriverDestroyAPIView(generics.DestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_field = 'id'
