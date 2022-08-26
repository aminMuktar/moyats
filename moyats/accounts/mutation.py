from email.policy import default
from pydoc import ModuleScanner
from urllib import response
import graphene
from .types import BaseUserType
from core.models import BaseContact
from core.helpers import(
    user_exists, org_exists, create_email_verification_link,
    is_valid_uuid, link_expired)
from django.contrib.auth import login
from accounts.inputs import NewUserInput, SocialRegistrationInput, UpdateUserInput
from accounts.models import BaseUser, EmailVerificationCode
from graphql_jwt.decorators import setup_jwt_cookie
from graphql_jwt import signals, mixins
from .decorators import jwt_token_auth, social_jwt_token_auth
from firebase_admin import auth
from django.contrib.auth.hashers import check_password, make_password


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

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(response=info.context.user)

    @classmethod
    @social_jwt_token_auth
    def mutate(cls, root, info, **kwargs):
        return cls.resolve(root, info, **kwargs)


class AddNewUser(graphene.Mutation):
    # New user registration mutation
    class Arguments:
        input = NewUserInput(required=True)

    response = graphene.Field(BaseUserType)

    def mutate(root, info, input: NewUserInput):
        if user_exists(input.email):
            raise Exception("E-mail is already registered")

        base_contact = BaseContact.objects.create(
            cell_number=input.first_name,
        )
        user = BaseUser.objects.create_user(
            email=input.email,
            username=input.email,
            first_name=input.first_name,
            last_name=input.last_name,
            password=input.password,
            base_contact=base_contact,
        )

        create_email_verification_link(user)
        return AddNewUser(response=user)

class UpdateUser(graphene.Mutation):
    response = graphene.List(BaseUserType)

    class Arguments:
        input = UpdateUserInput(required=True)


    def mutate(self, info, input: UpdateUserInput, **kwargs):
        change_user = BaseUser.objects.filter(user_id=info.context.user.user_id)
        contact_info = BaseContact.objects.filter(id=info.context.user.base_contact.id)
        

        change_user.update(
            first_name = input.first_name,
            last_name = input.last_name,
            username = input.username,
            email = input.email,
            # password = input.password,
            base_contact = contact_info.update(
                cell_number = input.cell_number,
                home_number = input.home_number,
                work_number = input.work_number
            )
        )

        return UpdateUser(response=change_user)

class CheckUserPassword(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        password = graphene.String()

    def mutate(self, info, password, **kwargs):
        check = check_password(password=password, encoded=info.context.user.password)

        return CheckUserPassword(response=check)

class ChangeUserPassword(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        password = graphene.String()

    def mutate(self, info, password, **kwargs):
        hash_password = make_password(password=password, salt=None, hasher="default")
        BaseUser.objects.update(
            password = hash_password
        )
        
        return ChangeUserPassword(response=True)
