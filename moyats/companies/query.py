import graphene
from . import types
from . import models
from core.helpers import core_paginator
from graphql_jwt.decorators import login_required
from django.db.models import Q


class CompanyQuery(graphene.ObjectType):
    companies = graphene.Field(
        types.CompanyPaginatedType, page_size=graphene.Int(), page=graphene.Int())
    company = graphene.Field(
        types.CompanyType, cid=graphene.String())

    contacts = graphene.Field(
        types.CompanyContactsPaginatedType, page_size=graphene.Int(), page=graphene.Int())
    contact = graphene.Field(
        types.CompanyContactType, cid=graphene.String())
    search_company = graphene.List(
        types.CompanyType, query=graphene.String()
    )
    search_company_contact = graphene.List(
        types.CompanyContactType, company=graphene.UUID(), query=graphene.String()
    )

    @login_required
    def resolve_search_company_contact(self, info, query, company, **kwargs):
        org = info.context.user.organizations.first()
        companies = models.Company.objects.filter(
            organization=org, company_id=company
        )
        if not companies.exists():
            raise Exception("company not found")
        contacts = models.CompanyContact.objects.filter(
            Q(company=companies.first()), Q(
                first_name__icontains=query) | Q(last_name__icontains=query)
        )
        return contacts

    @login_required
    def resolve_search_company(self, info, query, **kwargs):
        org = info.context.user.organizations.first()
        companies = models.Company.objects.filter(
            Q(organization=org), Q(name__icontains=query)
        )
        return companies

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
