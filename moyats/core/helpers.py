from accounts.models import BaseUser


def user_exists(email):
    user = BaseUser.objects.filter(email=email)
    return user.exists()
