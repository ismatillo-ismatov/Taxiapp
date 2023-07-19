from django.urls import path
from .views import DriverCreateAPIView, DriverListAPIView, DriverRetrieveAPIView, DriverUpdateAPIView, \
    DriverDestroyAPIView

app_name = 'driver'

urlpatterns = [
    path('drivers/create', DriverCreateAPIView.as_view(), name='driver-create'),
    path('drivers/', DriverListAPIView.as_view(), name="driver_list"),
    path('driver<int:pk>/', DriverRetrieveAPIView.as_view(), name="driver_datail"),
    path('driver/update<int:pk>', DriverUpdateAPIView.as_view(), name='driver-update'),
    path('drivers/delete/<int:pk>', DriverDestroyAPIView.as_view(), name='driver-delete'),

]