from rest_framework.serializers import ModelSerializer, ReadOnlyField

from apps.comments.models import Comment


class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.username')
    car = ReadOnlyField(source='car.id')

    class Meta:
        model = Comment
        fields = '__all__'
