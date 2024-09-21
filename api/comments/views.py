from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404

from .serializers import CommentSerializer
from apps.comments.models import Comment
from apps.cars.models import Car


class CommentList(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        car_id = self.kwargs['pk']
        get_object_or_404(Car, pk=self.kwargs['pk'])
        return Comment.objects.filter(car_id=car_id)

    def perform_create(self, serializer):
        car = get_object_or_404(Car, pk=self.kwargs['pk'])
        serializer.save(author=self.request.user,
                        car=car)
