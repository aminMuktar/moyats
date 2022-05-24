import graphene

from .types import BaseUserType
from core.models import BaseContact
from accounts.inputs import NewUserInput
from core.helpers import(
    user_exists, org_exists, create_email_verification_link,
    is_valid_uuid, link_expired)
from accounts.models import BaseUser, UserProfile, EmailVerificationCode


class VerifyEmail(graphene.Mutation):
    class Arguments:
        input = graphene.String()

    response = graphene.Boolean()

    def mutate(root, info, input):
        if not is_valid_uuid(input):
            raise Exception("Invalid Input")

        verificaiton_link = EmailVerificationCode.objects.filter(
            code_id=input
        )

        if verificaiton_link.first().used:
            raise Exception("Verification link has expired")

        if not verificaiton_link.exists():
            # TODO: add throttling for this condition to avoid bruteforces
            raise Exception("Verification code not found")

        if link_expired(verificaiton_link.first()):
            raise Exception("Verification link has expired")

        BaseUser.objects.filter(id=verificaiton_link.first().user.id).update(
            email_verified=True
        )
        verificaiton_link.update(used=True)
        return VerifyEmail(response=True)


class AddNewUser(graphene.Mutation):
    # New user registration mutation
    class Arguments:
        input = NewUserInput(required=True)

    response = graphene.Field(BaseUserType)

    def mutate(root, info, input: NewUserInput):
        if user_exists(input.email):
            raise Exception("E-mail is already registered")
        elif org_exists(input.company_title):
            raise Exception("Company is already registered")

        user_profile = UserProfile.objects.create(
            first_name=input.first_name,
            middle_name=input.middle_name,
            last_name=input.last_name,
        )
        base_contact = BaseContact.objects.create(
            cell_number=input.first_name,
        )
        user = BaseUser.objects.create_user(
            email=input.email,
            username=input.email,
            password=input.password,
            user_profile=user_profile,
            base_contact=base_contact,
        )
        user.organizations.create(
            name=input.company_title,
            verified=False,
            org_type=input.company_type.lower(),
            subdomain=input.subdomain
        )
        create_email_verification_link(user)
        return AddNewUser(response=user)
