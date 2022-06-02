import graphene
import graphql_jwt
from accounts.types import BaseUserType
from graphql_jwt.decorators import login_required
from accounts.mutation import AddNewUser, VerifyEmail, SocialMediaRegistration, BaseSocialLogin
from core.types import ActivityType
from core.models import Activity
from organizations.mutations import CreateOrganization


class Mutation(graphene.ObjectType):
    base_user_login = graphql_jwt.ObtainJSONWebToken.Field()
    base_user_logout = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    check_email_verification = VerifyEmail.Field()
    register = AddNewUser.Field()
    social_auth = SocialMediaRegistration.Field()
    setup_account = CreateOrganization.Field()


class Query(graphene.ObjectType):
    account_user = graphene.Field(BaseUserType)
    activities = graphene.List(ActivityType)

    @login_required
    def resolve_activities(self, info, **kwargs):
        return Activity.objects.all()

    @login_required
    def resolve_account_user(self, info, **kwargs):
        return info.context.user


schema = graphene.Schema(query=Query, mutation=Mutation)
