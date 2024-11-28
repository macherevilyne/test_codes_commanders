
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Orders


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['age']

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()  # Связанный профиль

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

# метод добавления новых пользователей
    def create(self, validated_data):
        # Создание пользователя с профилем
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user

# метод позволяет изменить существующие записи

    def update(self, instance, validated_data):
        # Обновление пользователя и профиля
        profile_data = validated_data.pop('profile', {})
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile = instance.profile
        profile.age = profile_data.get('age', profile.age)
        profile.save()

        return instance

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


# Метод для проверки существует ли пользователь при создании нового обьекта Order

    def validate_user(self, value):
        # Проверка существования пользователя
        if not User.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Пользователь с таким ID не существует.")
        return value