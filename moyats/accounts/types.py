from . import models
from core.models import BaseContact
from graphene_django import DjangoObjectType


class BaseUserType(DjangoObjectType):
    class Meta:
        model = models.BaseUser
        exclude = ("id", "password", "is_superuser", "is_staff")


class UserProfileType(DjangoObjectType):
    class Meta:
        model = models.UserProfile
        exclude = ("id",)


class BaseContactType(DjangoObjectType):
    class Meta:
        model = BaseContact
        exclude = ("id",)


class AddressType(DjangoObjectType):
    class Meta:
        model = models.Address
        exclude = ("id",)


class NotificationSettingType(DjangoObjectType):
    class Meta:
        model = models.NotificationSetting
        exclude = ("id",)
