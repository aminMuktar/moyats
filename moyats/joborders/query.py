import graphene
from . import types
from . import models
from core.helpers import core_paginator
from graphql_jwt.decorators import login_required


class JobOrderQuery(graphene.ObjectType):
    job_orders = graphene.Field(
        types.JobOrderPaginatedType, page_size=graphene.Int(), page=graphene.Int())

    @login_required
    def resolve_job_orders(self, info, page_size, page, **kwargs):
        job_orders = models.JobOrder.objects.all()
        return core_paginator(job_orders, page_size, page, types.JobOrderPaginatedType)
