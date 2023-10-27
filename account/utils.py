from django.utils.crypto import get_random_string


def generate_token():
    return get_random_string(length=32)


def generate_auth_number():
    return get_random_string(length=6, allowed_chars='1234567890')


def send_sms_message(phone_number, auth_number):
    message = {
        "message": {
            "phone_number": phone_number,
            "auth_number": auth_number
        }
    }
    return message


def send_token(token):
    return token
