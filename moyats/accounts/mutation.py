import graphene
from .types import BaseUserType
from core.helpers import user_exists
from accounts.inputs import NewUserInput
from accounts.models import BaseUser, UserProfile, BaseContact


class AddNewUser(graphene.Mutation):
    # New user registration mutation
    class Arguments:
        input = NewUserInput(required=True)

    response = graphene.Field(BaseUserType)

    def mutate(root, info, input: NewUserInput):
        if user_exists(input.email):
            raise Exception("E-mail is already registered")

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
        return AddNewUser(response=user)
