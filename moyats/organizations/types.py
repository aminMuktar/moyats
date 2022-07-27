import graphene
from . import models
from graphene_django import DjangoObjectType


class OrganizationType(DjangoObjectType):
    class Meta:
        model = models.Organization
        exclude = ("id",)


class OrganizationMemberType(DjangoObjectType):
    class Meta:
        model = models.OrganizationMember


class PortalType(DjangoObjectType):
    class Meta:
        model = models.Portal
