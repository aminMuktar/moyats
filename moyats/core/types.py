from . import models
from graphene_django import DjangoObjectType
from django.contrib.contenttypes.models import ContentType


class ContentObjectType(DjangoObjectType):
    class Meta:
        model = ContentType

class ActivityType (DjangoObjectType):
    class Meta:
        model = models.Activity
