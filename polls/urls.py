from django.urls import path
from . import views

urlpatterns = [
    # Добавляем путь для dataset
    path('dataset/', views.dataset_view, name='dataset'),  # путь для dataset
]