import graphene
from . import types
from . import models
from django.db.models import Q
from graphql_jwt.decorators import login_required


class PipelineQuery(graphene.ObjectType):
    pipeline_workflows = graphene.List(types.PipelineWorkflowType)

    @login_required
    def resolve_pipeline_workflows(self, info, **kwargs):
        org = info.context.user.organizations.first()
        return models.PipelineWorkflow.objects.filter(Q(default=True)|Q(organization=org))
