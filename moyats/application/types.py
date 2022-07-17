from graphene_django import DjangoObjectType
from . import models


class ApplicationType(DjangoObjectType):
    class Meta:
        model = models.Application


class ApplicationQuestionType(DjangoObjectType):
    class Meta:
        model = models.ApplicationQuestion
