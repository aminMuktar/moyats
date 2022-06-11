from .models import Application
from .types import ApplicationType
from graphql_jwt.decorators import login_required
import graphene


class ApplicationQuery(graphene.ObjectType):
    applications = graphene.List(ApplicationType)

    @login_required
    def resolve_applications(self, info, **kwargs):
        return Application.objects.all()
