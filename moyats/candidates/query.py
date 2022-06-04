import graphene
from .models import Candidate
from . import types
from core.helpers import core_paginator
from graphql_jwt.decorators import login_required


class CandidateQuery(graphene.ObjectType):
    candidtes = graphene.Field(
        types.CandidatesPaginatedType, page_size=graphene.Int(), page=graphene.Int())

    @login_required
    def resolve_candidtes(self, info, page_size, page, **kwargs):
        org = info.context.user.organizations.first()
        cands = Candidate.objects.filter(organization=org)
        return core_paginator(cands, page, page_size, types.CandidatesPaginatedType)
