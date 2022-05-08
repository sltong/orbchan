from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from boards import views as board_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("orbs.urls", namespace="orbs")),
    path("", include("boards.urls", namespace="boards")),
]

if settings.DEBUG == True:
    urlpatterns += [path("__reload__/", include("django_browser_reload.urls"))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
