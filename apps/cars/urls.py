from django.urls import path

from apps.cars.views import car_add, car_detail, car_delete, car_edit, index

urlpatterns = [
    path('', index, name='car-list'),
    path('car/<int:pk>', car_detail, name='car-detail'),
    path('car/<int:pk>/delete/', car_delete, name='car-delete'),
    path('car/<int:pk>/edit/', car_edit, name='car-edit'),
    path('car/add/', car_add, name='car-add'),

]
