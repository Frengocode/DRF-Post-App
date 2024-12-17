from rest_framework.generics import CreateAPIView, get_object_or_404, RetrieveAPIView
from rest_framework.viewsets import csrf_exempt
from django.contrib.auth.models import User
from .serializers import CreateUserSerializer, GetUserSerializers
from django.utils.decorators import method_decorator
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from utils.utils import log


@extend_schema(tags=["User"])
@method_decorator(csrf_exempt, name="dispatch")
class CreateUserAPIView(CreateAPIView):
    queryset = User
    serializer_class = CreateUserSerializer



@extend_schema(tags=["User"])
@method_decorator(csrf_exempt, name="dispatch")
class GetUserAPIView(RetrieveAPIView):
    serializer_class = GetUserSerializers
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = get_object_or_404(User, pk=self.kwargs.get("pk"))
        log.info("User getted succsesfully %s", user)
        return user


