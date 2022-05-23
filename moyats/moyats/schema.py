import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required


class Mutation(graphene.ObjectType):
    base_user_login = graphql_jwt.ObtainJSONWebToken.Field()
    base_user_logout = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    # TODO: remove these
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

class Query(graphene.ObjectType):
    test = graphene.String()

    @login_required
    def resolve_test(self, info, **kwargs):
        return info.context.user.email

schema = graphene.Schema(query=Query, mutation=Mutation)