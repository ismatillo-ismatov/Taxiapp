from django.urls import path
from .views import TripView

app_name = 'app'


urlpatterns = [
    path('',TripView.as_view({'get':'list'}),name='trip_list'),
    path('<int:pk>/',TripView.as_view({'get':'retrieve'}),name='trip_detail')
]