import uuid
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class BaseContact(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    cell_number = models.CharField(validators=[phone_regex], max_length=17)
    work_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, null=True)
    home_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.cell_number)

class UserProfile(models.Model):
    profile_pic = models.ImageField(upload_to='uploads/% Y/% m/% d/', null=True, blank=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name()


class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.country


class NotificationSetting(models.Model):
    class NotificaionSettingType(models.TextChoices):
        SEND_EMAIL = 'se', _('Send Email')
        SEND_PUSH = 'sp', _('Send Push')

    setting = models.CharField(choices=NotificaionSettingType.choices, max_length=2)
    value = models.BooleanField(default=True)
    updated_At = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.setting


class BaseUser(AbstractUser):
    class AccountType(models.TextChoices):
        ADMIN = 'ad', _('Admin')
        BASE_USER = 'bu', _('Basic User')
        SYS_EDITOR = 'sy', _('System Editor')
        PREMIUM_USER = 'pu', _('Premium User')

    class AccountSource(models.TextChoices):
        EMAIL = 'em', _('Email')
        GOOGLE = 'go', _('Google')
        LINKEDIN = 'ln', _('LinkedIn')
        GITHUB = 'gh', _('Github')

    base_contact = models.ForeignKey(
        BaseContact, on_delete=models.CASCADE, null=True)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True)
    account_type = models.CharField(
        choices=AccountType.choices, max_length=2, default=AccountType.BASE_USER)
    source = models.CharField(
        choices=AccountSource.choices, max_length=2, default=AccountSource.EMAIL)
    organizations = models.ManyToManyField("organizations.Organization", blank=True)
    blocked = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    signiture = models.TextField(null=True, blank=True)
    notification_setting = models.ForeignKey(
        NotificationSetting, on_delete=models.CASCADE, null=True, blank=True)
    timezone = models.CharField(max_length=200, blank=True, null=True)
    date_format = models.CharField(max_length=100, blank=True, null=True)
    updated_At = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return str(self.email)

class EmailVerificationCode(models.Model):
    code_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    expiry_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.code_id

