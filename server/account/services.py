from account.models import AccountUser


def create_account_user(username: str, password: str):
    is_user = AccountUser.objects.get(username=username).exists()

    if is_user:
        raise Exception("이미 존재하는 유저입니다.")

    user = AccountUser.objects.create(username=username, password=password)

    return user
