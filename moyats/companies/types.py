import graphene
from . import models
from graphene_django import DjangoObjectType


class CompanyContactStatusType(DjangoObjectType):
    class Meta:
        model = models.CompanyContactStatus


class CompanyContactType(DjangoObjectType):
    class Meta:
        model = models.CompanyContact


class CompanyStatusType(DjangoObjectType):
    class Meta:
        model = models.CompanyStatus


class CompanyType(DjangoObjectType):
    contacts = graphene.List(CompanyContactType)

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
