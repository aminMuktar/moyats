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


class ActivityType(DjangoObjectType):
    content_object = GenericScalar()

    def resolve_content_object(parent, info):
        serialized_obj = serializers.serialize(
            'json', [parent.content_object, ])
        serialized = json.loads(serialized_obj)[0]["fields"]
        all_keys = serialized.keys()
        excluded = ["password", "email", "notification_setting", "setup_complete", "timezone",
                    "date_format", "updated_At", "groups", "user_permissions", "organizations",
                    "blocked", "email_verified", "is_superuser", "is_staff", "is_active", "date_joined",
                    "updated_at"]
        for ky in excluded:
            if ky in all_keys:
                del serialized[ky]
        return serialized

    class Meta:
        model = models.Activity


class ActivityPaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    objects = graphene.List(ActivityType)
    total = graphene.Int()
