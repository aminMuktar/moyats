import graphene
from . import types
from core.helpers import core_paginator
from .models import Candidate, CandidateSource
from graphql_jwt.decorators import login_required


class CandidateQuery(graphene.ObjectType):
    candidtes = graphene.Field(
        types.CandidatesPaginatedType, page_size=graphene.Int(), page=graphene.Int())
    candidate_sources = graphene.List(types.CandidateSourceType)

    @login_required
    def resolve_candidate_sources(self, info, **kwargs):
        return CandidateSource.objects.all()

    @login_required
    def resolve_candidtes(self, info, page_size, page, **kwargs):
        org = info.context.user.organizations.first()
        cands = Candidate.objects.filter(organization=org)
        return core_paginator(cands, page_size, page, types.CandidatesPaginatedType)
