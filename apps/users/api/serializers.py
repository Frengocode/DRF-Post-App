from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied
from utils.utils import log



class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, attrs):
        # Получаем пароли
        password1 = attrs.get("password1")
        password2 = attrs.get("password2")

        # Проверка на совпадение паролей
        if password1 != password2:
            log.error("Passwords do not match")
            raise serializers.ValidationError({"password": "Passwords do not match"})

        # Проверка уникальности имени пользователя
        if User.objects.filter(username=attrs.get("username")).exists():
            log.error("Username already taken")
            raise serializers.ValidationError({"username": "This username is already taken!"})

        return attrs  # Возвращаем все аттрибуты без изменений, если валидация прошла успешно

    def create(self, validated_data):
        # Убираем password2, так как оно не нужно при создании пользователя
        password = validated_data.pop("password1")

        # Создаем нового пользователя, передавая только необходимые поля
        user = User.objects.create(username=validated_data["username"])

        # Устанавливаем зашифрованный пароль
        user.set_password(password)
        user.save()

        log.info("User created successfully %s", user)
        return user




class GetUserSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
