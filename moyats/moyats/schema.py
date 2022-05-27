import graphene
import graphql_jwt

from accounts.types import BaseUserType
from graphql_jwt.decorators import login_required
from accounts.models import EmailVerificationCode
from core.helpers import is_valid_uuid, link_expired
from accounts.mutation import AddNewUser, VerifyEmail, SocialMediaRegistration, SocialMediaLogin


class Mutation(graphene.ObjectType):
    base_user_login = graphql_jwt.ObtainJSONWebToken.Field()
    base_user_logout = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    social_login = SocialMediaLogin.Field()
    check_email_verification = VerifyEmail.Field()
    register = AddNewUser.Field()
    social_auth = SocialMediaRegistration.Field()


class Query(graphene.ObjectType):
    account_user = graphene.Field(BaseUserType)
    test = graphene.String()

    def resolve_test(self, info, **kwargs):
        return "hey there"

    @login_required
    def resolve_account_user(self, info, **kwargs):
        return info.context.user


schema = graphene.Schema(query=Query, mutation=Mutation)
