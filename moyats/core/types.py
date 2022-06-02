import json
import graphene
from . import models
from django.core import serializers
from graphene_django import DjangoObjectType
from graphene.types.generic import GenericScalar
from django.contrib.contenttypes.models import ContentType


class ContentObjectType(DjangoObjectType):
    class Meta:
        model = ContentType


class ActivityType (DjangoObjectType):
    content_object = GenericScalar()

    def resolve_content_object(parent, info):
        serialized_obj = serializers.serialize(
            'json', [parent.content_object, ])
        serialized = json.loads(serialized_obj)[0]["fields"]
        return serialized

    class Meta:
        model = models.Activity
