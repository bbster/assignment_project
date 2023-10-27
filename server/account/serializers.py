from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class SessionSerializer(serializers.Serializer):
    token = serializers.CharField()
    auth_number = serializers.CharField()