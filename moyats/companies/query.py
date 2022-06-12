import graphene
from . import types
from . import models
from core.helpers import core_paginator
from graphql_jwt.decorators import login_required


class CompanyQuery(graphene.ObjectType):
    companies = graphene.Field(
        types.CompanyPaginatedType, page_size=graphene.Int(), page=graphene.Int())
    company = graphene.Field(
        types.CompanyType, cid=graphene.String())

    contacts = graphene.Field(
        types.CompanyContactsPaginatedType, page_size=graphene.Int(), page=graphene.Int())
    contact = graphene.Field(
        types.CompanyContactType, cid=graphene.String())

    @login_required
    def resolve_company(self, info, cid, **kwargs):
        org = info.context.user.organizations.first()
        company = models.Company.objects.filter(
            company_id=cid, organization=org
        )
        if not company.exists():
            raise Exception("invalid input")
        return company.first()

    @login_required
    def resolve_contact(self, info, cid, **kwargs):
        org = info.context.user.organizations.first()
        contacts = models.CompanyContact.objects.filter(
            company__organization=org, company_contact_id=cid)
        return contacts.first()

    @login_required
    def resolve_companies(self, info, page_size, page, **kwargs):
        org = info.context.user.organizations.first()
        companies = models.Company.objects.filter(organization=org)
        return core_paginator(companies, page_size, page, types.CompanyPaginatedType)

    @login_required
    def resolve_contacts(self, info, page_size, page, **kwargs):
        org = info.context.user.organizations.first()
        contacts = models.CompanyContact.objects.filter(
            company__organization=org)
        return core_paginator(contacts, page_size, page, types.CompanyContactsPaginatedType)
