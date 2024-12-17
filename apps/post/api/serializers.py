from rest_framework import serializers
from ..models import Post
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied


class UserSerialzier(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    user = UserSerialzier()
    created_at = serializers.DateTimeField()


class CreatePostSerialzier(serializers.Serializer):
    title = serializers.CharField()

    def create(self, validated_data):
        user = self.context["request"].user
        return Post.objects.create(**validated_data, user=user)


class UpdatePostSerialzers(serializers.Serializer):
    title = serializers.CharField()

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    def validate(self, data):
        request = self.context.get("request")
        instance = self.instance

        if request.user != instance.user:
            raise PermissionDenied(
                {"message": "You do not have permission to update this post."}
            )

        return data
