from . import models
from graphene_django import DjangoObjectType

class PipelineWorkflowType(DjangoObjectType):
    class Meta:
        model = models.PipelineWorkflow
    
