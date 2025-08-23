# blog/urls.py
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, RegisterView
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"comments", CommentViewSet, basename="comment")

app_name = "v1"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("jwt-create/", TokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt-refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("", include(router.urls)),
]
