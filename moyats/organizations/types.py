import graphene
from . import models
from graphene_django import DjangoObjectType


class OrganizationType(DjangoObjectType):
    class Meta:
        model = models.Organization
        exclude = ("id","org_id",)
