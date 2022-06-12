import graphene
from .types import BaseUserType
from graphql_jwt.decorators import login_required


class AccountsQuery(graphene.ObjectType):
    account_user = graphene.Field(BaseUserType)
    username = graphene.Field(graphene.String)

    @login_required
    def resolve_account_user(self, info, **kwargs):
        return info.context.user

    @login_required
    def resolve_username(self, info, **kwargs):
        return info.context.user.username
