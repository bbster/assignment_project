from datetime import timedelta

from django.contrib.auth import authenticate, get_user_model, login
from django.http import HttpResponse
from django.utils.timezone import now
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import AccountUser
from account.serializers import SessionSerializer, TokenSerializer, AccountLoginSerializer
from account.utils import (
    generate_auth_number,
    generate_auth_token,
    send_auth_number,
)


#
# class TokenAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = TokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         username = serializer.validated_data["username"]
#         password = serializer.validated_data["password"]
#
#         user = get_user_model().objects.get(username=username)
#
#         if user.check_password(password):
#             # 토큰 발급
#             auth_number = generate_auth_number()
#             token = generate_auth_token()
#             expired_at = now() + timedelta(seconds=5)
#             Token.objects.update_or_create(
#                 user=user,
#                 defaults={
#                     "token": token,
#                     "expired_at": expired_at,
#                     "auth_number": auth_number,
#                 },
#             )
#
#             # 인증번호 발송
#             phone_number = "010-1234-5678"
#             send_auth_number(phone_number, user.username, auth_number)
#
#             return Response({"token": token}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 {"message": "인증 실패!"},
#                 status=status.HTTP_401_UNAUTHORIZED,
#             )
#
#
# class SessionAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = SessionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         token = serializer.validated_data["token"]
#         auth_number = serializer.validated_data["auth_number"]
#
#         token = Token.objects.filter(
#             token=token,
#         ).first()
#
#         if not token:
#             return Response(
#                 {"message": "올바른 토큰이 아닙니다."},
#                 status=status.HTTP_401_UNAUTHORIZED,
#             )
#
#         if auth_number != token.auth_number:
#             return Response(
#                 {"message": "인증번호가 틀립니다."},
#                 status=status.HTTP_401_UNAUTHORIZED,
#             )
#
#         is_expired = token.expired_at <= now()
#         if is_expired:
#             return Response(
#                 {"message": "인증시간이 만료 되었습니다."},
#                 status=status.HTTP_401_UNAUTHORIZED,
#             )
#
#         user = token.user
#
#         # 로그인 처리
#         login(request, user)
#
#         return Response(
#             {"message": "로그인 성공"},
#             status=status.HTTP_201_CREATED,
#         )


class AccountCreateView(CreateAPIView):
    queryset = AccountUser.objects.all()
    serializer_class = AccountLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 사용자 인증
        user = authenticate(request, username=serializer.validated_data["username"], password=serializer.validated_data["password"])

        if user is not None:
            # 로그인
            login(request, user)
            return Response({"message": "로그인 성공"}, status=status.HTTP_200_OK,)
        else:
            return Response({"message": "로그인 실패"}, status=status.HTTP_400_BAD_REQUEST,)
