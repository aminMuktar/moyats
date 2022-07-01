import graphene
from .utils import get_type
from graphene_file_upload.scalars import Upload
from .models import Candidate, CandidateSource, SocialMedia
from .inputs import CandidateInput, CandidatePrimaryInput
from accounts.models import Address, BaseContact
from .models import CandidateProfile
from .types import CandidateType
from core.helpers import (
    org_exists,
)


class UpdateCandidateDetail(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        # input = CandidateDetailInput()
        candidate = graphene.UUID()

    def mutate(self, info, status, candidate, **kwargs):
        return UpdateCandidateDetail(response=True)


class UpdateCandidatePrimary(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        input = CandidatePrimaryInput()
        candidate = graphene.UUID()

    def mutate(self, info, input: CandidatePrimaryInput, candidate, **kwargs):
        cand = Candidate.objects.filter(candidate_id=candidate)
        if not cand.exists():
            raise Exception("Candidate not found")
        # check for null
        if input.address:
            address = Address.objects.filter(id=input.address)
            if not address.exists():
                raise Exception("Address not found")
            cand.update(address=address.first())
        if input.social_medias:
            for sm in input.social_medias:
                cand.first().social_medias.create(link=sm.link, type=sm.type)

        cand_profile = CandidateProfile.objects.filter(
            id=cand.first().candidate_profile.id
        )
        if cand_profile.exists():
            cand_profile.update(
                first_name=input.candidate_profile.first_name if input.candidate_profile.first_name else cand_profile.first().first_name,
                last_name=input.candidate_profile.last_name if input.candidate_profile.last_name else cand_profile.first().last_name,
                middle_name=input.candidate_profile.middle_name if input.candidate_profile.middle_name else cand_profile.first().middle_name,
                email=input.candidate_profile.email if input.candidate_profile.email else cand_profile.first().email
            )
        else:
            cand.candidate_profile.create(
                first_name=input.candidate_profile.first_name,
                last_name=input.candidate_profile.last_name,
                middle_name=input.candidate_profile.middle_name,
                email=input.candidate_profile.email
            )
        phones = cand.first().phones
        if not phones:
            bcontact = BaseContact.objects.create(
                cell_number=input.phones.cell_number,
                work_number=input.phones.work_number,
                home_number=input.phones.home_number
            )
            cand.update(phones=bcontact)
        else:
            bcontact = BaseContact.objects.filter(id=phones.id)
            bcontact.update(
                cell_number=input.phones.cell_number if input.phones.cell_number else phones.cell_number,
                work_number=input.phones.work_number if input.phones.work_number else phones.work_number,
                home_number=input.phones.home_number if input.phones.home_number else phones.home_number,
            )

        return UpdateCandidatePrimary(response=True)


class AddCandidate(graphene.Mutation):
    response = graphene.Field(CandidateType)

    class Arguments:
        input = CandidateInput()
        attachments = Upload(required=True)

    def mutate(self, info, input: CandidateInput, attachments: Upload, **kwargs):
        org = info.context.user.organizations.first()
        contact = BaseContact.objects.filter(
            cell_number=input.cell_phone
        )
        if not contact.exists():
            contact.create(cell_number=input.cell_phone)

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

        address = Address.objects.filter(
            city=input.city,
            country=input.country
        )

        if not address.exists():
            address.create(
                city=input.city,
                country=input.country)

        source = CandidateSource.objects.filter(
            id=input.source
        )

        if not source.exists():
            raise Exception("Source does not exist")

        candidate = Candidate.objects.create(
            candidate_profile=candidteProfile.first(),
            organization=org,
            phones=contact.first(),
            address=address.first(),
            source=source.first(),
            key_skills=input.keySkills,
            current_employeer=input.currentEmployeer,
            current_pay=input.currentPay,
            desired_pay=input.desiredPay,
            website=input.website,
        )
        for at in attachments:
            candidate.attachments.create(
                filename=at._name,
                file=at,
                is_resume=False
            )

        for sm in input.socialMedias:
            candidate.social_medias.create(
                type=get_type(sm.link), link=sm.link)
        return AddCandidate(response=candidate)
