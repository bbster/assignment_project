import random

from django.utils.crypto import get_random_string


def generate_auth_token():
    return get_random_string(length=20)


def generate_auth_number():
    return str(random.randrange(100000, 1000000))


def make_sms_message(user_name, auth_number):
    message = f"{user_name}님, 로그인을 위한 인증번호는 {auth_number} 입니다."
    return message


def send_auth_number(phone_number, user_name, auth_number):
    message = make_sms_message(user_name, auth_number)

    SMSAPI.send(phone_number, message)

    return auth_number


class SMSAPI:
    @classmethod
    def send(cls, phone_number, message):
        print("SMS를 발송합니다.")
        print("수신자", phone_number)
        print("내용", message)
        print("SMS를 발송했습니다.")
