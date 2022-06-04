import graphene
from . import models
from graphene_django import DjangoObjectType


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
    class Meta:
        model = models.Candidate


class CandidatesPaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    objects = graphene.List(CandidateType)
    total = graphene.Int()
