from django.urls import path
from . import views

urlpatterns = [
    path("", views.direcciones, name="direcciones"),
]
