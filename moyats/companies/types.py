import graphene
from accounts.models import BaseUser
from . import models
from accounts.types import BaseUserType
from graphene_django import DjangoObjectType
from joborders.models import JobOrder


class CompanyContactStatusType(DjangoObjectType):
    class Meta:
        model = models.CompanyContactStatus


class CompanyContactType(DjangoObjectType):
    owner = graphene.Field(BaseUserType)

    def resolve_owner(parent, info):
        if parent.company:
            owner = BaseUser.objects.filter(
                organizations__id=parent.company.organization.id)
            return owner.first()
        return None

    class Meta:
        model = models.CompanyContact


class CompanyStatusType(DjangoObjectType):
    class Meta:
        model = models.CompanyStatus


class CompanyType(DjangoObjectType):
    contacts = graphene.List(CompanyContactType)
    owner = graphene.Field(BaseUserType)
    contacts_count = graphene.Int()
    joborders_count = graphene.Int()

    def resolve_joborders_count(parent, info):
        return JobOrder.objects.filter(company__id=parent.id).count()

    def resolve_contacts_count(parent, info):
        return models.CompanyContact.objects.filter(company__id=parent.id).count()

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
