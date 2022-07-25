from copyreg import constructor
import graphene
from . import types
from . import models
from django.db.models import Q
from core.types import EnumType
from application.types import ApplicationType
from application.models import Application
from core.helpers import core_paginator
from graphql_jwt.decorators import login_required
from .enums import PositionTypes
from organizations.types import OrganizationMemberType


class JobOrderQuery(graphene.ObjectType):
    job_orders = graphene.Field(
        types.JobOrderPaginatedType,
        page_size=graphene.Int(), page=graphene.Int())
    job_order = graphene.Field(
        types.JobOrderType,
        id=graphene.String()
    )
    position_types = graphene.List(EnumType)
    joborder_types = graphene.List(types.JobOrderTypesType)
    joborder_status = graphene.List(types.JoborderStatusType)
    joborder_applications = graphene.List(ApplicationType)
    joborder_application = graphene.Field(
        ApplicationType, application=graphene.String())
    categories = graphene.List(types.JobOrderCategoryType)
    search_recruiter = graphene.List(
        OrganizationMemberType, query=graphene.String())
    joborder_applicant_pipeline = graphene.Field(
        types.JobOrderApplicantPaginatedType, joborder=graphene.String(),
        page=graphene.Int(), page_size=graphene.Int())

    @login_required
    def resolve_joborder_applicant_pipeline(self, info, joborder, page, page_size, **kwargs):
        org = info.context.user.organizations.first()
        joborder_q = models.JobOrder.objects.filter(
            organization=org, joborder_id=joborder
        )
        if not joborder_q.exists():
            return core_paginator([], page_size, page, types.JobOrderApplicantPaginatedType)
        pipeline_qset = joborder_q.first(
        ).pipeline_workflow.candidates.filter(joborder=joborder_q.first())
        return core_paginator(pipeline_qset, page_size, page, types.JobOrderApplicantPaginatedType)

    @login_required
    def resolve_search_recruiter(self, info, query):
        org = info.context.user.organizations.first()
        members = org.members.filter(
            Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query))
        return members

    @login_required
    def resolve_categories(self, info, **kwargs):
        return models.JobOrderCategory.objects.all()

    @login_required
    def resolve_joborder_application(self, info, application, **kwargs):
        org = info.context.user.organizations.first()
        applications = Application.objects.filter(
            organization=org, application_id=application)
        if not applications.exists():
            raise Exception("Application not found")
        return applications.first()

    @login_required
    def resolve_joborder_applications(self, info, **kwargs):
        org = info.context.user.organizations.first()
        applications = Application.objects.filter(
            organization=org).order_by("-created_at")
        return applications

    @login_required
    def resolve_joborder_status(self, info, **kwargs):
        return models.JoborderStatus.objects.all()

    @login_required
    def resolve_joborder_types(self, info, **kwargs):
        return models.JobOrderTypes.objects.all()

    @login_required
    def resolve_position_types(self, info, **kwargs):
        pos_types = [{'id': year[0], 'label': year[1]}
                     for year in PositionTypes.choices]
        return pos_types

    @login_required
    def resolve_job_order(self, info, id, **kwargs):
        org = info.context.user.organizations.first()
        joborder = models.JobOrder.objects.filter(
            organization=org, joborder_id=id)
        if not joborder.exists():
            raise Exception("job order not found")
        return joborder.first()

    @login_required
    def resolve_job_orders(self, info, page_size, page, **kwargs):
        org = info.context.user.organizations.first()
        job_orders = models.JobOrder.objects.filter(
            organization=org).order_by('-created_at')
        return core_paginator(job_orders, page_size, page, types.JobOrderPaginatedType)
