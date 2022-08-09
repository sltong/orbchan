from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from orbs.views import home, boards, board, create_thread


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("<slug:board_slug>/", board, name="board"),
    path("<slug:board_slug>/create_thread/", create_thread, name="create_thread"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
