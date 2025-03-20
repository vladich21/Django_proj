from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path("dataset/", include('polls.urls')),
]

# python manage.py makemigrations
# python manage.py migrateк