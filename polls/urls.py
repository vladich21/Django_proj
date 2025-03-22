from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import UserViewSet, ContainerViewSet, RentalViewSet, SibTransLogViewSet, NotificationViewSet
from .views import dataset_view

# Роутер для API
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'containers', ContainerViewSet)
router.register(r'rentals', RentalViewSet)
router.register(r'sibtranslogs', SibTransLogViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('dataset/', dataset_view, name='dataset_view'),  # HTML-шаблон
    path('api/', include(router.urls)),  # API через DRF
]



