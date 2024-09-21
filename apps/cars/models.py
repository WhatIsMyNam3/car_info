from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.db import models


class Car(models.Model):
    """Модель машины."""
    make = models.CharField(
        verbose_name='Марка автомобиля',
        max_length=20
    )
    model = models.CharField(
        verbose_name='Модель автомобиля',
        max_length=20
    )
    year = models.PositiveIntegerField(
        verbose_name='Год выпуска',
        validators=[
            MinValueValidator(1884),
            MaxValueValidator(date.today().year)
        ]
    )
    description = models.TextField(
        verbose_name='Описание автомобиля',
    )
    created_at = models.DateTimeField(
        verbose_name='Дата и время создания записи',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата и время последнего обновления записи',
        auto_now=True
    )
    owner = models.ForeignKey(
        get_user_model(),
        verbose_name='Владелец автомобиля',
        on_delete=models.CASCADE,
        related_name='cars'
    )

    def __str__(self) -> str:
        return f'{self.make} {self.model}, {self.year}'
