import graphene

from accounts.models import BaseUser
from . import models
from accounts.types import BaseUserType
from graphene_django import DjangoObjectType
from organizations.models import Organization
from pipelines.types import PipelineWorkflowType


class JoborderStatusType(DjangoObjectType):
    class Meta:
        model = models.JoborderStatus


class JobOrderTypesType(DjangoObjectType):
    class Meta:
        model = models.JobOrderTypes


class JobOrderCategoryType(DjangoObjectType):
    class Meta:
        model = models.JobOrderCategory


class JobDetailType(DjangoObjectType):
    class Meta:
        model = models.JobDetail


class JobOrderType(DjangoObjectType):
    owner = graphene.Field(BaseUserType)

    def resolve_owner(parent, info):
        owner = BaseUser.objects.filter(
            organizations__id=parent.organization.id)
        return owner.first()

    class Meta:
        model = models.JobOrder


class JobOrderPaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    objects = graphene.List(JobOrderType)
    total = graphene.Int()
