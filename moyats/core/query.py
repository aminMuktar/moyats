import graphene
from .models import Activity
from .helpers import core_paginator
from .types import ActivityPaginatedType, UniqueActivityType
from graphql_jwt.decorators import login_required
from .types import NotificationType
from .models import Notification


class CoreQuery(graphene.ObjectType):
    activities = graphene.Field(
        ActivityPaginatedType, page_size=graphene.Int(), page=graphene.Int())
    activity = graphene.Field(
        UniqueActivityType, activity_id=graphene.String()
    )

    @login_required
    def resolve_activity(self, info, activity_id, **kwargs):
        activity_info = Activity.objects.filter(
            activity_id=activity_id, user=info.context.user)
        return activity_info.first()

    @login_required
    def resolve_activities(self, info, page_size, page, **kwargs):
        all_activities = Activity.objects.filter(
            user=info.context.user, activity_type='ca').order_by("-created_at")
        print(all_activities, "all acts")
        return core_paginator(all_activities, page_size, page, ActivityPaginatedType)

class NotificationQuery(graphene.ObjectType):
    notification = graphene.List(NotificationType)

    def resolve_notification(self, info):
        return Notification.objects.all()
