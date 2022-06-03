from . import models
from graphene_django import DjangoObjectType


class TriggerType(DjangoObjectType):
    class Meta:
        model = models.Trigger


class PipelineStatusType(DjangoObjectType):
    class Meta:
        model = models.PipelineStatus

class PipelineSetupType(DjangoObjectType):
    class Meta:
        model = models.PipelineSetup

class PipelineWorkflowType(DjangoObjectType):
    class Meta:
        model = models.PipelineWorkflow
