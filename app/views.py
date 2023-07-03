from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, viewsets,permissions
from .serializer import UserSerializer, LoginSerializer,TripSerializer
from .models import Trip


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LogInView(TokenObtainPairView):
    serializer_class = LoginSerializer

class TripView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer