from django.urls import path

from .views import index


app_name = "orbs"

urlpatterns = [
    path("", index),
]
