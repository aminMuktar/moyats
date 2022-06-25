import string
import graphene

from core.models import BaseContact
from accounts.models import BaseUser, Address
from graphene_file_upload.scalars import Upload
from .models import Company, CompanyContact, CompanyContactStatus, CompanyStatus
from .inputs import CompanyPrimaryInfoUpdateInput, ContactPrimaryInfoUpdateInput
from graphql_jwt.decorators import login_required


class ContactPrimaryInfoUpdateMutation(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        input = ContactPrimaryInfoUpdateInput()

    def mutate(self, info, input: ContactPrimaryInfoUpdateInput, **kwargs):
        contacts = CompanyContact.objects.filter(
            company_contact_id=input.contact)
        if not contacts.exists():
            raise Exception("contact not found")
        contacts.update(first_name=input.name.first_name,
                        last_name=input.name.last_name,
                        )
        return ContactPrimaryInfoUpdateMutation(response=True)


class CompanyContactStatusUpdate(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        contact = graphene.String()
        status = graphene.Int()

    @login_required
    def mutate(self, info, contact, status, **kwargs):
        contacts = CompanyContact.objects.filter(
            company_contact_id=contact)
        if not contacts.exists():
            raise Exception("contact not found")
        stat = CompanyContactStatus.objects.filter(id=status)
        if not stat.exists():
            raise Exception("status not found")

        contacts.update(status=stat.first())
        return CompanyContactStatusUpdate(response=True)


class UpdateContactCompany(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        contact = graphene.String()
        company = graphene.String()

    @login_required
    def mutate(self, info, contact, company, **kwargs):
        contacts = CompanyContact.objects.filter(
            company_contact_id=contact)
        if not contacts.exists():
            raise Exception("contact not found")
        comp = Company.objects.filter(company_id=company)
        if not comp.exists():
            raise Exception("company not found")

        contacts.update(company=comp.first())
        return UpdateContactCompany(response=True)


class UpdateContactReport(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        contact = graphene.String()
        report_to = graphene.Int()

    @login_required
    def mutate(self, info, contact, report_to, **kwargs):
        contacts = CompanyContact.objects.filter(
            company_contact_id=contact)
        if not contacts.exists():
            raise Exception("contact not found")
        report = BaseUser.objects.filter(id=report_to)
        if not report.exists():
            raise Exception("user not found")

        contacts.update(contact_reports_to=report.first())
        return UpdateContactReport(response=True)


class UpdateContactNote(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        contact = graphene.String()
        note = graphene.String()

    @login_required
    def mutate(self, info, contact, note, **kwargs):
        contacts = CompanyContact.objects.filter(
            company_contact_id=contact)
        if not contacts.exists():
            raise Exception("contact not found")

        contacts.update(notes=note)
        return UpdateContactNote(response=True)


class UpdateCompanyPrimary(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        input = CompanyPrimaryInfoUpdateInput()

    @login_required
    def mutate(self, info, input: CompanyPrimaryInfoUpdateInput, **kwargs):
        company = Company.objects.filter(
            company_id=input.company)
        if not company.exists():
            raise Exception("company not found")
        contact = BaseContact.objects.create(
            cell_number=input.phones.cell_phone
        )
        address = Address.objects.filter(id=input.address)
        company.update(website=input.website, name=input.name,
                       phones=contact, address=address.first())
        return UpdateContactNote(response=True)


class UpdateCompanyStatus(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        company = graphene.String()
        status = graphene.Int()

    @login_required
    def mutate(self, info, company, status, ** kwargs):
        company = Company.objects.filter(
            company_id=company)
        if not company.exists():
            raise Exception("company not found")
        stat = CompanyStatus.objects.filter(id=status)
        if not stat.exists():
            raise Exception("status not found")

        company.update(company_status=stat.first())
        return UpdateContactNote(response=True)


class UpdateCompanyNotes(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        company = graphene.String()
        note = graphene.String()

    @login_required
    def mutate(self, info, company, note, **kwargs):
        comp = Company.objects.filter(company_id=company)
        if not comp.exists():
            raise Exception("company not found")

        comp.update(notes=note)
        return UpdateCompanyNotes(response=True)


class AddCompanyAttachments(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        file = Upload(required=True)
        company = graphene.String()
        filename = graphene.String()
        is_resume = graphene.Boolean()

    @login_required
    def mutate(self, info, file, company, filename, is_resume, **kwargs):
        comp = Company.objects.filter(company_id=company)
        if not comp.exists():
            raise Exception("company not found")
        comp.first().attachments.create(file=file, filename=filename, is_resume=is_resume)
        return AddCompanyAttachments(response=True)
