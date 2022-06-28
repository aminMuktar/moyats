import graphene
import graphql_jwt
from core.query import CoreQuery
from accounts.query import AccountsQuery
from organizations.mutations import CreateOrganization
from organizations.query import OrganizationQuery
from pipelines.query import PipelineQuery
from companies.query import CompanyQuery
from joborders.query import JobOrderQuery
from candidates.query import CandidateQuery
from application.query import ApplicationQuery
from candidates.mutation import (
    AddCandidate,
    UpdateCandidatePrimary,
    UpdateCandidateDetail
)
from joborders.mutations import (
    AddJobOrder,
    UpdateJobOrderPrimary,
    UpdateJobOrderStatus,
    UpdateJobOrderDetails,
    UpdateJoborderDescription,
    UpdateJoborderNotes,
    UpdateJoborderApplication,
    AddJobOrderAttachments,
    UpdateJobOrderCompany
)

from companies.mutations import(
    UpdateCompanyPrimary,
    ContactPrimaryInfoUpdateMutation,
    CompanyContactStatusUpdate,
    UpdateContactCompany,
    UpdateContactReport,
    UpdateContactNote,
    UpdateCompanyStatus,
    UpdateCompanyNotes,
    AddCompanyAttachments,
)
from accounts.mutation import AddNewUser, VerifyEmail, SocialMediaRegistration


class Query(ApplicationQuery, AccountsQuery, CoreQuery, OrganizationQuery, JobOrderQuery, PipelineQuery, CompanyQuery, CandidateQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    base_user_login = graphql_jwt.ObtainJSONWebToken.Field()
    base_user_logout = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    check_email_verification = VerifyEmail.Field()
    register = AddNewUser.Field()
    social_auth = SocialMediaRegistration.Field()
    setup_account = CreateOrganization.Field()
    add_candidate = AddCandidate.Field()
    add_joborder = AddJobOrder.Field()
    # contact mutations
    update_contact_primary = ContactPrimaryInfoUpdateMutation.Field()
    update_contact_status = CompanyContactStatusUpdate.Field()
    update_contact_company = UpdateContactCompany.Field()
    update_contact_report = UpdateContactReport.Field()
    update_contact_note = UpdateContactNote.Field()
    # companies mutations
    update_company_primary = UpdateCompanyPrimary.Field()
    update_company_status = UpdateCompanyStatus.Field()
    update_company_notes = UpdateCompanyNotes.Field()
    add_company_attachment = AddCompanyAttachments.Field()
    # joborder mutations
    update_joborder_primary = UpdateJobOrderPrimary.Field()
    update_joborder_status = UpdateJobOrderStatus.Field()
    update_joborder_details = UpdateJobOrderDetails.Field()
    update_joborder_description = UpdateJoborderDescription.Field()
    update_joborder_notes = UpdateJoborderNotes.Field()
    update_joborder_application = UpdateJoborderApplication.Field()
    update_joborder_attachments = AddJobOrderAttachments.Field()
    update_joborder_company = UpdateJobOrderCompany.Field()
    #  candidates mutations
    update_candidate_primary = UpdateCandidatePrimary.Field()
    update_candidate_detail = UpdateCandidateDetail.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
