import os
import firebase_admin
from .models import BaseUser
from graphql_jwt import signals
from graphql_jwt import exceptions
from firebase_admin import auth, credentials
from django.contrib.auth import get_user_model
from graphene.utils.thenables import maybe_thenable
from graphql_jwt.decorators import wraps, setup_jwt_cookie, csrf_rotation, refresh_expiration, on_token_auth_resolve

if not firebase_admin._apps:
    cred = credentials.Certificate(os.environ.get("FIREBASE_KEY_PATH"))
    default_app = firebase_admin.initialize_app(cred)


def social_jwt_token_auth(f):
    @wraps(f)
    @setup_jwt_cookie
    @csrf_rotation
    @refresh_expiration
    def wrapper(cls, root, info, **kwargs):
        input = kwargs.get("input")
        context = info.context
        # context._jwt_token_auth = True

        uid = None
        decoded = None
        try:
            decoded_token = auth.verify_id_token(input.access_token)
            uid = decoded_token['uid']
            decoded = decoded_token
        except Exception as e:
            raise Exception(f"Invalid token {e}")

        user_search = BaseUser.objects.filter(access_token=uid)
        if user_search.exists():
            user = user_search.first()
            if hasattr(info.context, "user"):
                info.context.user = user

            signals.token_issued.send(
                sender=cls, request=info.context, user=user)

            if hasattr(context, "user"):
                context.user = user

            result = f(cls, root, info, **kwargs)
            signals.token_issued.send(sender=cls, request=context, user=user)

            return maybe_thenable((context, user, result), on_token_auth_resolve)

        first, last = None, None
        if decoded["name"]:
            first, last = decoded["name"].split(" ")

        user = BaseUser.objects.create_user(
            email=decoded["email"],
            access_token=uid,
            first_name=first if first is not None else "",
            last_name=last if last is not None else "",
            username=decoded["email"],
            user_profile=user_profile,
            source=input.source
        )
        if hasattr(info.context, "user"):
            info.context.user = user

        signals.token_issued.send(
            sender=cls, request=info.context, user=user)

        if hasattr(context, "user"):
            context.user = user

        result = f(cls, root, info, **kwargs)
        signals.token_issued.send(sender=cls, request=context, user=user)

        return maybe_thenable((context, user, result), on_token_auth_resolve)
    return wrapper


def jwt_token_auth(f):
    @wraps(f)
    @setup_jwt_cookie
    @csrf_rotation
    @refresh_expiration
    def wrapper(cls, root, info, **kwargs):
        context = info.context
        context._jwt_token_auth = True
        # check access token status and verify user
        access_token = kwargs.get("access_token")
        decoded_token = auth.verify_id_token(access_token)
        uid = decoded_token['uid']
        userq = BaseUser.objects.filter(access_token=uid)
        user = userq.first()

        if hasattr(info.context, "user"):
            info.context.user = user

        signals.token_issued.send(sender=cls, request=info.context, user=user)

        if hasattr(context, "user"):
            context.user = user

        result = f(cls, root, info, **kwargs)
        signals.token_issued.send(sender=cls, request=context, user=user)
        return maybe_thenable((context, user, result), on_token_auth_resolve)

    return wrapper
