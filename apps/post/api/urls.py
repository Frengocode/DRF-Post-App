from django.urls import path
from .views import (
    CreatePostApiView,
    GetPosts,
    GetPostAPIView,
    UpdatePostAPIView,
    DeletePostAPIView,
)

urlpatterns = [
    path("create-post/", CreatePostApiView.as_view()),
    path("get-posts/", GetPosts.as_view()),
    path("get-post/<int:pk>/", GetPostAPIView.as_view()),
    path("update-post/<int:pk>/", UpdatePostAPIView.as_view()),
    path("delete-post/<int:pk>/", DeletePostAPIView.as_view()),
]
