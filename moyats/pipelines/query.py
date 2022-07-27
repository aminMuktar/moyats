import graphene
from . import types
from . import models
from django.db.models import Q
from graphql_jwt.decorators import login_required


class PipelineQuery(graphene.ObjectType):
    pipeline_workflows = graphene.List(types.PipelineWorkflowType)
    pipeline_workflow_setup = graphene.List(
        types.PipelineSetupType, workflow=graphene.UUID())

    @login_required
    def resolve_pipeline_workflow_setup(self, info, workflow, **kwargs):
        org = info.context.user.organizations.first()
        pipeline = models.PipelineWorkflow.objects.filter(
            organization=org, pipeline_id=workflow)
        if not pipeline.exists():
            raise Exception("Pipeline not found")
        return pipeline.first().pipeline_setups.all()

    @login_required
    def resolve_pipeline_workflows(self, info, **kwargs):
        org = info.context.user.organizations.first()
        return models.PipelineWorkflow.objects.filter(Q(default=True) | Q(organization=org))
