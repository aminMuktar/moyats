import graphene
import graphql_jwt
from .types import BaseUserType
from core.models import BaseContact
from core.helpers import(
    user_exists, org_exists, create_email_verification_link,
    is_valid_uuid, link_expired)
from django.contrib.auth import login
from accounts.inputs import NewUserInput, SocialRegistrationInput
from accounts.models import BaseUser, UserProfile, EmailVerificationCode
from graphql_jwt.decorators import setup_jwt_cookie
from graphql_jwt import signals, mixins
from .decorators import jwt_token_auth
# import firebase_admin
from firebase_admin import auth


# firebase_admin.initialize_app()

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


class JSONWebTokenMutation(mixins.ObtainJSONWebTokenMixin, graphene.Mutation):
    class Meta:
        abstract = True

    @classmethod
    def Field(cls, *args, **kwargs):
        cls._meta.arguments.update(
            {
                "username": graphene.String(required=False),
                "password": graphene.String(required=False),
            },
        )
        return super().Field(*args, **kwargs)

    @classmethod
    @jwt_token_auth
    def mutate(cls, root, info, **kwargs):
        return cls.resolve(root, info, **kwargs)


class BaseSocialLogin(JSONWebTokenMutation):
    user = graphene.Field(BaseUserType)

    class Arguments:
        access_token = graphene.String(required=False)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)


class SocialMediaRegistration(graphene.Mutation):
    class Arguments:
        input = SocialRegistrationInput(required=True)

    response = graphene.Field(BaseUserType)

    def mutate(root, info, input: SocialRegistrationInput):
        # if user_exists(input.email):
        #     raise Exception("E-mail is already registered")
        uid = None
        try:
            decoded_token = auth.verify_id_token(input.access_token)
            uid = decoded_token['uid']
        except Exception:
            raise Exception("Invalid token")

        user_search = BaseUser.objects.filter(access_token=uid)
        if user_search.exists():
            raise Exception("User already exists")

        user_profile = UserProfile.objects.create(
            first_name=input.first_name,
            last_name=input.last_name,
        )
        # base_contact = BaseContact.objects.create(
        #     cell_number=input.first_name,
        # )
        user = BaseUser.objects.create_user(
            email=input.email,
            access_token=uid,
            username=input.email,
            user_profile=user_profile,
            source=input.source
            # base_contact=base_contact,
        )
        return SocialMediaRegistration(response=user)


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
        # user.organizations.create(
        #     name=input.company_title,
        #     verified=False,
        #     org_type=input.company_type.lower(),
        #     subdomain=input.subdomain
        # )
        create_email_verification_link(user)
        return AddNewUser(response=user)
