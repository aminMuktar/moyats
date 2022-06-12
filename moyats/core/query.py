import graphene
from .models import Activity
from .helpers import core_paginator
from .types import ActivityPaginatedType
from graphql_jwt.decorators import login_required


class CoreQuery(graphene.ObjectType):
    activities = graphene.Field(
        ActivityPaginatedType, page_size=graphene.Int(), page=graphene.Int())

    @login_required
    def resolve_activities(self, info, page_size, page, **kwargs):
        all_activities = Activity.objects.filter(user=info.context.user)
        return core_paginator(all_activities, page_size, page, ActivityPaginatedType)
