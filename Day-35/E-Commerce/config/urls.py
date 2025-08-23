from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("shop.urls")),   # version 1
    path("api/v2/", include("shop.urls")),   # version 2 (future)
]
