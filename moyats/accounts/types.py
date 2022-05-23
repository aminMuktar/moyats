from . import models
from graphene_django import DjangoObjectType


class BaseUserType(DjangoObjectType):
    class Meta:
        model = models.BaseUser
