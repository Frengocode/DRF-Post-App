from django.urls import path
from .views import CreateUserAPIView, GetUserAPIView


urlpatterns = [
    path("create-user/", CreateUserAPIView.as_view()),
    path("get-user/<int:pk>/", GetUserAPIView.as_view()),
]
