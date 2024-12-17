from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    GenericAPIView,
    UpdateAPIView,
)
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from .serializers import PostSerializer, CreatePostSerialzier, UpdatePostSerialzers
from ..models import Post
from rest_framework.exceptions import NotFound
from utils.utils import log
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView


@extend_schema(tags=["Post"])
class CreatePostApiView(CreateAPIView):
    queryset = Post
    serializer_class = CreatePostSerialzier
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["Post"])
class GetPosts(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["Post"])
class GetPostAPIView(GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        try:
            post = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(post)
            log.info("Post Getted Succsesfully %s status", 200)
            return Response(serializer.data, status=200)

        except Post.DoesNotExist:
            raise NotFound({"messsage": "Post Not Found"})


@extend_schema(tags=["Post"])
class UpdatePostAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = UpdatePostSerialzers
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["Post"])
class DeletePostAPIView(GenericAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        try:
            post = self.get_queryset().get(pk=pk, user=request.user)
            post.delete()
            return Response({"message": "Deleted Successfully"}, status=200)

        except Post.DoesNotExist:
            raise NotFound({"message": "Post Not Found"})
