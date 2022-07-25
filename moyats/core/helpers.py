import json
import uuid
import pytz
import math
from datetime import datetime
from core.models import Color
from datetime import timedelta
from django.core import serializers
from organizations.models import Organization
from accounts.models import BaseUser, EmailVerificationCode, BaseContact, Address
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from candidates.models import SocialMedia, CandidateProfile, Candidate
from joborders.models import JobDetail, JoborderStatus


def serialize_object(obj):
    serialized_obj = serializers.serialize(
        'json', [obj, ])
    serialized_ = json.loads(serialized_obj)[0]["fields"]
    return serialized_


def get_job_details(id):
    obj = JobDetail.objects.get(id=id)
    return serialize_object(obj)


def get_candidate_profile(id):
    obj = CandidateProfile.objects.get(id=id)
    return serialize_object(obj)


def dig_deep(a_type, serialized):
    if a_type == "jo":
        serialized["job_detail"] = get_job_details(serialized["job_detail"])
    if a_type == "ca":
        serialized["candidate_profile"] = get_candidate_profile(
            serialized["candidate_profile"])
    return serialized


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


def social_media_exists(socialType):
    socialM = SocialMedia.objects.filter(type=socialType)
    return socialM.exists()


def phone_exists(phone):
    phoneC = BaseContact.objects.filter(phone=phone)
    return phoneC.exists()


def address_exists(address):
    addressC = Address.objects.filter(address=address)
    return addressC.exists()


def candidate_exist(firstName, middleName, lastName):
    cand_exist = CandidateProfile.objects.filter(
        first_name=firstName,
        middle_name=middleName,
        last_name=lastName
    )
    return cand_exist.exists()
