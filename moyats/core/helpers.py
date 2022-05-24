import uuid
import pytz
from datetime import datetime
from datetime import timedelta
from organizations.models import Organization
from accounts.models import BaseUser, EmailVerificationCode


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
    utc=pytz.UTC
    date = verification.expiry_date
    has_expired = utc.localize(datetime.now()) > date
    return has_expired
