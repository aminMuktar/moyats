import graphene
from . import types
from . import models
from core.helpers import core_paginator
from graphql_jwt.decorators import login_required


class CompanyQuery(graphene.ObjectType):
    companies = graphene.Field(
        types.CompanyPaginatedType, page_size=graphene.Int(), page=graphene.Int())
    contacts = graphene.Field(
        types.CompanyContactsPaginatedType, page_size=graphene.Int(), page=graphene.Int())

    @login_required
    def resolve_companies(self, info, page_size, page, **kwargs):
        org = info.context.user.organizations.first()
        companies = models.Company.objects.filter(organization=org)
        return core_paginator(companies, page, page_size, types.CompanyPaginatedType)

    @login_required
    def resolve_contacts(self, info, page_size, page, **kwargs):
        org = info.context.user.organizations.first()
        contacts = models.CompanyContact.objects.filter(
            company__organization=org)
        return core_paginator(contacts, page, page_size, types.CompanyContactsPaginatedType)
