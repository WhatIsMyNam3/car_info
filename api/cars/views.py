from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from apps.cars.models import Car
from .serializers import CarSerializer
from ..permissions import IsAdminOrOwnerOrReadOnly


class CarList(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CarDetail(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminOrOwnerOrReadOnly
    ]
