import graphene
import graphql_jwt
from core.query import CoreQuery
from accounts.query import AccountsQuery
from organizations.mutations import CreateOrganization
from accounts.mutation import AddNewUser, VerifyEmail, SocialMediaRegistration
from organizations.query import OrganizationQuery
from pipelines.query import PipelineQuery
from companies.query import CompanyQuery
from joborders.query import JobOrderQuery
from candidates.query import CandidateQuery
from application.query import ApplicationQuery


class Query(ApplicationQuery, AccountsQuery, CoreQuery, OrganizationQuery, JobOrderQuery, PipelineQuery, CompanyQuery, CandidateQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    base_user_login = graphql_jwt.ObtainJSONWebToken.Field()
    base_user_logout = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    check_email_verification = VerifyEmail.Field()
    register = AddNewUser.Field()
    social_auth = SocialMediaRegistration.Field()
    setup_account = CreateOrganization.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
