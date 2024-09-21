from django.urls import path

from apps.cars.views import index, car_detail

urlpatterns = [
    path('', index, name='car-list'),
    path('cars/<int:pk>', car_detail, name='car-detail'),
]
