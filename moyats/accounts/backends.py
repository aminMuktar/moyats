from .models import BaseUser
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = BaseUser.objects.get(email=username)
        except BaseUser.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None