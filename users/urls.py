from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('me/', views.get_user, name='get_user'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]