import json
from .models import BaseUser
from graphql_jwt import signals
from graphql_jwt import exceptions
from graphql_jwt.decorators import wraps, setup_jwt_cookie, csrf_rotation, refresh_expiration, on_token_auth_resolve
from django.contrib.auth import get_user_model
from graphene.utils.thenables import maybe_thenable
import firebase_admin
from firebase_admin import auth


firebase_admin.initialize_app()


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
