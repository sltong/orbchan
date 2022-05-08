from django.urls import path

from .views import (
    index,
    board_detail,
)


app_name = "boards"

urlpatterns = [
    path("", index),
    path("<slug:board_slug>/", board_detail, name="board_detail"),
]
