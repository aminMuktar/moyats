import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required

from accounts.types import BaseUserType
from accounts.mutation import AddNewUser


class Mutation(graphene.ObjectType):
    base_user_login = graphql_jwt.ObtainJSONWebToken.Field()
    base_user_logout = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    register = AddNewUser.Field()

class Query(graphene.ObjectType):
    account_user = graphene.Field(BaseUserType)

    @login_required
    def resolve_account_user(self, info, **kwargs):
        return info.context.user

schema = graphene.Schema(query=Query, mutation=Mutation)