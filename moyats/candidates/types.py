import graphene
from . import models
from graphene_django import DjangoObjectType
from pipelines.models import PipelineWorkflow
from pipelines.types import PipelineWorkflowType
from joborders.types import JobOrderType
from joborders.models import JobOrder


class AttachmentType(DjangoObjectType):
    class Meta:
        model = models.Attachment


class CandidateSourceType(DjangoObjectType):
    class Meta:
        model = models.CandidateSource


class SocialMediaTypes(DjangoObjectType):
    class Meta:
        model = models.SocialMedia


class CandidateProfileType(DjangoObjectType):
    class Meta:
        model = models.CandidateProfile


class WorkHistoryType(DjangoObjectType):
    class Meta:
        model = models.WorkHistory


class QualificationChecklistType(DjangoObjectType):
    class Meta:
        model = models.QualificationChecklist


class CandidateQualificationType(DjangoObjectType):
    class Meta:
        model = models.CandidateQualification


class CandidateType(DjangoObjectType):
    pipeline = graphene.Field(PipelineWorkflowType)
    latest_joborder = graphene.Field(JobOrderType)

    class Meta:
        model = models.Candidate

    def resolve_pipeline(parent, info):
        pipeline = PipelineWorkflow.objects.filter(
            candidates__id=parent.id
        )
        if not pipeline.exists():
            return None

        return pipeline.first()

    def resolve_latest_joborder(parent, info):
        pipeline = PipelineWorkflow.objects.filter(
            candidates__id=parent.id
        )
        if not pipeline.exists():
            return None

        joborder = JobOrder.objects.filter(
            pipeline_workflow=pipeline.first()
        )
        jo = joborder.latest('created_at')
        if not joborder.exists:
            return None
        return jo


class CandidatesPaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    objects = graphene.List(CandidateType)
    total = graphene.Int()
