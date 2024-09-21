from django.contrib.auth import get_user_model
from django.db import models

from ..cars.models import Car


class Comment(models.Model):
    """Модель комментария."""
    content = models.TextField(verbose_name='Содержание комментария')
    created_at = models.DateTimeField(
        verbose_name='Дата и время создания комментария',
        auto_now_add=True
    )
    car = models.ForeignKey(
        Car,
        verbose_name='Машина, которую комментируют',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        get_user_model(),
        verbose_name='Автор комментария',
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self) -> str:
        return self.content
