# books_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Path-versioned API (URL Path versioning)
    path("api/<version>/", include("books.urls")),

    # Non-path entry (supports query param and header versioning)
    path("api/", include("books.urls")),
]
