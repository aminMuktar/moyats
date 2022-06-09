import graphene
from . import types
from . import models
from core.helpers import core_paginator
from graphql_jwt.decorators import login_required


class JobOrderQuery(graphene.ObjectType):
    job_orders = graphene.Field(
        types.JobOrderPaginatedType,
        page_size=graphene.Int(), page=graphene.Int())
    job_order = graphene.Field(
        types.JobOrderType,
        id=graphene.String()
    )

    @login_required
    def resolve_job_order(self, info, id, **kwargs):
        org = info.context.user.organizations.first()
        joborder = models.JobOrder.objects.filter(organization=org, joborder_id=id)
        if not joborder.exists():
            raise Exception("job order not found")
        return joborder.first()

    @login_required
    def resolve_job_orders(self, info, page_size, page, **kwargs):
        org = info.context.user.organizations.first()
        job_orders = models.JobOrder.objects.filter(organization=org)
        return core_paginator(job_orders, page_size, page, types.JobOrderPaginatedType)
