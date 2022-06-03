import graphene
from . import models
from graphene_django import DjangoObjectType


class JobOrderTypeModelDefinition(DjangoObjectType):
    class Meta:
        model = models.JobOrderType


class JobOrderCategoryType(DjangoObjectType):
    class Meta:
        model = models.JobOrderCategory


class JobDetailType(DjangoObjectType):
    class Meta:
        model = models.JobDetail

class JobOrderObjectType(DjangoObjectType):
    class Meta:
        model = models.JobOrder

class JobOrderPaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    objects = graphene.List(JobOrderObjectType)
    total = graphene.Int()


