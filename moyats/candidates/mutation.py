import graphene
from .utils import get_type
from core.views import create_candidate_activity
from graphene_file_upload.scalars import Upload
from .models import Candidate, CandidateSource
from accounts.models import Address, BaseContact
from .models import CandidateProfile
from .types import CandidateType
from .inputs import CandidateDetailInput, CandidateInput, CandidatePrimaryInput, CandidateWorkHistoryInput


class RemoveCandidateWorkHistory(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        candidate = graphene.UUID()
        whid = graphene.Int()

    def mutate(self, info, candidate, whid, **kwargs):
        org = info.context.user.organizations.first()
        cand = Candidate.objects.filter(
            candidate_id=candidate, organization=org)
        if not cand.exists():
            raise Exception("candidate not found")
        cand.first().work_history.filter(id=whid).delete()
        return RemoveCandidateWorkHistory(response=True)


class UpdateCandidateWorkHistory(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        candidate = graphene.UUID()
        input = CandidateWorkHistoryInput()
        whistory = graphene.Int()

    def mutate(self, info, candidate, input: CandidateWorkHistoryInput, whistory, **kwargs):
        org = info.context.user.organizations.first()
        cand = Candidate.objects.filter(
            candidate_id=candidate, organization=org)
        if not cand.exists():
            raise Exception("candidate not found")
        workhistory = cand.first().work_history.filter(id=whistory)
        if not workhistory.first():
            raise Exception("work history not found")

        workhistory.update(
            title=input.title if input.title else workhistory.first().title,
            employeer=input.employeer if input.employeer else workhistory.first().employeer,
            start_date=input.start_date if input.start_date else workhistory.first().start_date,
            end_date=input.end_date if input.end_date else workhistory.first().end_date,
            reason_for_leaving=input.leaving_reason if input.leaving_reason else workhistory.first().reason_for_leaving,
            currently_working=input.currently_working if input.currently_working else workhistory.first().currently_working
        )

        return UpdateCandidateWorkHistory(response=True)


class AddCandidateWorkHistory(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        candidate = graphene.UUID()
        input = CandidateWorkHistoryInput()

    def mutate(self, info, candidate, input: CandidateWorkHistoryInput, **kwargs):
        org = info.context.user.organizations.first()
        cand = Candidate.objects.filter(
            candidate_id=candidate, organization=org)
        if not cand.exists():
            raise Exception("candidate not found")
        cand.first().work_history.create(title=input.title, employeer=input.employeer,
                                         currently_working=input.currently_working,
                                         start_date=input.start_date, reason_for_leaving=input.leaving_reason,
                                         end_date=input.end_date if input.end_date else None)

        return AddCandidateWorkHistory(response=True)


class UpdateCandidateNotes(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        notes = graphene.String(required=True)
        candidate = graphene.UUID()

    def mutate(self, info, notes, candidate, **kwargs):
        org = info.context.user.organizations.first()
        cand = Candidate.objects.filter(
            candidate_id=candidate, organization=org)
        if not cand.exists():
            raise Exception("Candidate not found")
        cand.update(notes=notes)
        return UpdateCandidateNotes(response=True)


class UpdateCandidateDetail(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        input = CandidateDetailInput(required=True)
        candidate = graphene.UUID()

    def mutate(self, info, input: CandidateDetailInput, candidate, **kwargs):
        org = info.context.user.organizations.first()
        cand = Candidate.objects.filter(
            candidate_id=candidate, organization=org)
        if not cand.exists():
            raise Exception("Candidate not found")
        # check for null
        source = CandidateSource.objects.filter(id=input.source)
        if not source.exists():
            raise Exception("Candidate source not found")
        cand.update(key_skills=input.key_skills, current_employeer=input.current_employeer,
                    desired_pay=input.desired_pay, current_pay=input.current_pay,
                    date_available=input.date_available,
                    source=source.first())

        return UpdateCandidateDetail(response=True)


class UpdateCandidatePrimary(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        input = CandidatePrimaryInput()
        candidate = graphene.UUID()

    def mutate(self, info, input: CandidatePrimaryInput, candidate, **kwargs):
        org = info.context.user.organizations.first()
        cand = Candidate.objects.filter(
            candidate_id=candidate, organization=org)
        if not cand.exists():
            raise Exception("Candidate not found")
        # check for null
        addr = None
        address = Address.objects.filter(
            country=input.country, city=input.city)
        if not address.exists():
            addr = Address.objects.create(
                country=input.country, city=input.city)
        else:
            addr = address.first()

        cand.update(address=addr)
        # if input.social_medias:
        #     for sm in input.social_medias:
        #         cand.first().social_medias.create(link=sm.link, type=sm.type)

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
                last_name=input.lastName,
                email=input.email
            )

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
            notes=input.notes,
            phones=contact.first(),
            address=address.first(),
            source=source.first(),
            key_skills=input.keySkills,
            current_employeer=input.currentEmployeer,
            current_pay=input.currentPay,
            desired_pay=input.desiredPay,
            website=input.website,
        )
        annotation = f"Added candidiate {candidate.candidate_profile.first_name} {candidate.candidate_profile.last_name}"
        create_candidate_activity(
            candidate, "nw", annotation, info.context.user)
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
