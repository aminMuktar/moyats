import graphene
from accounts.models import BaseUser
from . import models
from accounts.types import BaseUserType
from graphene_django import DjangoObjectType


class CompanyContactStatusType(DjangoObjectType):
    class Meta:
        model = models.CompanyContactStatus


class CompanyContactType(DjangoObjectType):
    owner = graphene.Field(BaseUserType)

    def resolve_owner(parent, info):
        owner = BaseUser.objects.filter(
            organizations__id=parent.company.organization.id)
        return owner.first()

    class Meta:
        model = models.CompanyContact


class CompanyStatusType(DjangoObjectType):
    class Meta:
        model = models.CompanyStatus


class CompanyType(DjangoObjectType):
    contacts = graphene.List(CompanyContactType)
    owner = graphene.Field(BaseUserType)

    def resolve_owner(parent, info):
        owner = BaseUser.objects.filter(
            organizations__id=parent.organization.id)
        return owner.first()

    def resolve_contacts(parent, info):
        contacts = models.CompanyContact.objects.filter(company__id=parent.id)
        return contacts

    class Meta:
        model = models.Company


class CompanyPaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    objects = graphene.List(CompanyType)
    total = graphene.Int()


class CompanyContactsPaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    objects = graphene.List(CompanyContactType)
    total = graphene.Int()
