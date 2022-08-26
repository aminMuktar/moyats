import json
from this import d
import graphene

from . import models
from .helpers import dig_deep
from django.core import serializers
from graphene_django import DjangoObjectType
from graphene.types.generic import GenericScalar
from django.contrib.contenttypes.models import ContentType


class ColorType(DjangoObjectType):
    class Meta:
        model = models.Color


class ContentObjectType(DjangoObjectType):
    class Meta:
        model = ContentType


class ActivityType(DjangoObjectType):
    content_object = GenericScalar()

    class Meta:
        model = models.Activity

    def resolve_content_object(parent, info):
        serialized_obj = serializers.serialize(
            'json', [parent.content_object, ])
        serialized_ = json.loads(serialized_obj)[0]["fields"]
        print(parent.activity_type, "Info")
        serialized = dig_deep(parent.activity_type, serialized_)
        all_keys = serialized.keys()
        excluded = [
            "password", "email", "notification_setting", "setup_complete", "timezone",
            "date_format", "updated_At", "groups", "user_permissions", "organizations",
            "blocked", "email_verified", "is_superuser", "is_staff", "is_active", "date_joined",
            "updated_at"
        ]

        for ky in excluded:
            if ky in all_keys:
                del serialized[ky]
        return serialized


class ActivityPaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    objects = graphene.List(ActivityType)
    total = graphene.Int()


class UniqueActivityType(graphene.ObjectType):
    activity = graphene.Field(ActivityType)

    def resolve_activity(parent, info, **kwargs):
        owner = models.Activity.objects.filter(
            user=parent.user,
            activity_id=parent.activity_id
        )
        return owner.first()

    class Meta:
        model = models.Activity


class EnumType(graphene.ObjectType):
    id = graphene.String()
    label = graphene.String()


class NotificationType(DjangoObjectType):
    class Meta:
        model = models.Notification


