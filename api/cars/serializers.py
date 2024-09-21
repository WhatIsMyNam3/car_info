from rest_framework.serializers import ModelSerializer, ReadOnlyField

from apps.cars.models import Car


class CarSerializer(ModelSerializer):
    owner = ReadOnlyField(source='owner.username')

    class Meta:
        model = Car
        fields = '__all__'
