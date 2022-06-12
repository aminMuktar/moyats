import graphene
from .utils import get_type
from organizations.models import Organization
from .models import Candidate, CandidateSource, SocialMedia
from .inputs import CandidateInput
from accounts.models import Address, BaseContact
from .models import CandidateProfile
from .types import CandidateType
from core.helpers import (
    org_exists,
)


class AddCandidate(graphene.Mutation):
    response = graphene.Field(CandidateType)

    class Arguments:
        input = CandidateInput()

    def mutate(self, info, input: CandidateInput):

        contact = BaseContact.objects.filter(
            cell_number=input.phone
        )
        if not contact.exists():
            contact.create()

        candidteProfile = CandidateProfile.objects.filter(
            first_name=input.firstName,
            middle_name=input.middleName,
            last_name=input.lastName,
        )
        if not candidteProfile.exists():
            CandidateProfile.objects.create(
                first_name=input.firstName,
                middle_name=input.middleName,
                last_name=input.lastName,)

        # if not social_media_exists(input.socialMediaType):
        #     raise Exception("Socal does not exist")

        if not org_exists(input.organization):
            raise Exception("Organization does not exist")

        address = Address.objects.filter(
            city=input.city,
            zip_code=input.zipCode,
            country=input.country
        )

        if not address.exists():
            address.create(
                city=input.city,
                zip_code=input.zipCode,
                country=input.country)

        source = CandidateSource.objects.filter(
            name=input.source
        )
        if not source.exists():
            raise Exception("Source does not exist")

        organization = Organization.objects.filter(
            name=input.organization
        )

        add_candidate = Candidate.objects.create(
            candidate_profile=candidteProfile.first(),
            organization=organization.first(),
            phones=contact.first(),
            address=address.first(),
            key_skills=input.keySkills,
            current_employeer=input.currentEmployeer,
            current_pay=input.currentPay,
            desired_pay=input.desiredPay,
            website=input.website,
        )
        for sm in input.socialMedias:
            add_candidate.social_medias.create(
                type=get_type(sm.link), link=sm.link)
        return AddCandidate(response=add_candidate)