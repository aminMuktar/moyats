import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()

class Query(graphene.ObjectType):
    test = graphene.String()

    @login_required
    def resolve_test(self, info, **kwargs):
        return info.context.user.email

schema = graphene.Schema(query=Query, mutation=Mutation)