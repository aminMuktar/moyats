import graphene
import graphql_jwt
from accounts.types import BaseUserType
from graphql_jwt.decorators import login_required
from accounts.mutation import AddNewUser, VerifyEmail, SocialMediaRegistration
from core.types import ActivityPaginatedType
from core.models import Activity
from core.helpers import core_paginator
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
    activities = graphene.Field(
        ActivityPaginatedType, page_size=graphene.Int(), page=graphene.Int())

    @login_required
    def resolve_activities(self, info, page_size, page, **kwargs):
        all_activities = Activity.objects.all()
        return core_paginator(all_activities, page_size, page, ActivityPaginatedType)

    @login_required
    def resolve_account_user(self, info, **kwargs):
        return info.context.user


schema = graphene.Schema(query=Query, mutation=Mutation)
