from django.forms import CharField, ModelForm, IntegerField
from apps.cars.models import Car


class CarAddForm(ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'description',)
