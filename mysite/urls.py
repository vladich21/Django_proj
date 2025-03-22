from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),  # Подключаем маршруты для polls
    path("admin/", admin.site.urls),  # Админ-панель
    path("", include("polls.urls")),  # Убери dataset, подключи просто все маршруты из polls
]