import uuid
import pytz
import math
from datetime import datetime
from datetime import timedelta
from organizations.models import Organization
from accounts.models import BaseUser, EmailVerificationCode
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def user_exists(email):
    user = BaseUser.objects.filter(email=email)
    return user.exists()


def org_exists(name):
    org = Organization.objects.filter(name=name)
    return org.exists()


def create_email_verification_link(user):
    link_expiry_hours_limit = 3
    origin_date = datetime.now()
    hours_forward = origin_date + timedelta(hours=link_expiry_hours_limit)
    verification = EmailVerificationCode.objects.create(
        user=user,
        expiry_date=hours_forward
    )
    return verification


def is_valid_uuid(value):
    try:
        uuid.UUID(value)

        return True
    except ValueError:
        return False


def link_expired(verification: EmailVerificationCode):
    # covert to naive or aware datetime objects.
    utc = pytz.UTC
    date = verification.expiry_date
    has_expired = utc.localize(datetime.now()) > date
    return has_expired


def core_paginator(qs, page_size, page, paginated_type, **kwargs):
    p = Paginator(qs, page_size)

    try:
        page_obj = p.page(page)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    return paginated_type(
        page=page_obj.number,
        pages=p.num_pages,
        total=math.ceil(qs.count()/page_size),
        has_next=page_obj.has_next(),
        has_prev=page_obj.has_previous(),
        objects=page_obj.object_list,
        **kwargs
    )
