from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .cars.views import CarDetail, CarList
from .comments.views import CommentList


urlpatterns = [
    path('cars/', CarList.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetail.as_view(), name='car-detail'),
    path('cars/<int:pk>/comments/', CommentList.as_view(), name='comment-list'),
    path('token/', obtain_auth_token)
]
