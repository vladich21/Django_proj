# import datetime
from django.db import models
# from django.utils import timezone
import uuid

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Container(models.Model):
    container_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Уникальный идентификатор")
    type = models.CharField(max_length=255, verbose_name="Тип контейнера")
    status = models.CharField(max_length=255, verbose_name="Статус контейнера")
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текущее местоположение")
    owner_id = models.UUIDField(blank=True, null=True, verbose_name="Связь с владельцем")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    def __str__(self):
        return f"{self.type} - {self.status}"

        class Rental(models.Model):
    rental_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Уникальный идентификатор")
    container = models.ForeignKey('Container', on_delete=models.CASCADE, verbose_name="Контейнер")
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Пользователь")
    start_date = models.DateTimeField(verbose_name="Дата начала аренды")
    end_date = models.DateTimeField(verbose_name="Дата окончания аренды")
    status = models.CharField(max_length=255, verbose_name="Статус аренды")
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Суточная ставка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Rental {self.rental_id} - {self.status}"