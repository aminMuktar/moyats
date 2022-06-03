import graphene
from . import models
from graphene_django import DjangoObjectType
from pipelines.types import PipelineWorkflowType

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
    class Meta:
        model = models.JobOrder

class JobOrderPaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    objects = graphene.List(JobOrderType)
    total = graphene.Int()


