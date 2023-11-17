from rest_framework import serializers

from account.models import AccountUser


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class SessionSerializer(serializers.Serializer):
    token = serializers.CharField()
    auth_number = serializers.CharField()


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountUser
        fields = ['username', 'password']
