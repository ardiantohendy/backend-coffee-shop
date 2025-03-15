from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'items', views.MenuItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get/', views.get_data)
]