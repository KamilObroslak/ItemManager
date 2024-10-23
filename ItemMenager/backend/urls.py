from django.urls import path

from . import views
from .views import create_user

urlpatterns = [
    path("test", views.index, name="index"),
    path('api/create_user', create_user, name='create_user'),
]

