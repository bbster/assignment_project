from rest_framework import serializers


class CreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=100)


class SessionSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)
    token = serializers.CharField(max_length=100)
    auth_number = serializers.CharField(max_length=100)