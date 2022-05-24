import uuid
from django.db import models
from core.models import BaseContact, Color
from django.utils.translation import gettext_lazy as _


class OrganizationStatus(models.Model):
    name = models.CharField(max_length=300)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    default = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class OrganizationContact(models.Model):
    phones = models.ForeignKey(
        BaseContact, on_delete=models.CASCADE, null=True)
    reachable = models.BooleanField(default=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email


class OrganizationMember(models.Model):
    class OrganizationMemberPermission(models.TextChoices):
        OWNER = 'ow', _('Is Owner')
        ADMIN = 'ad', _('Is Admin')
        EDITOR = 'ed', _('Is Editor')
        READ_ONLY = 'ro', _('Read Only')

    user = models.ForeignKey("accounts.BaseUser", on_delete=models.CASCADE, null=True)
    title = models.CharField(null=True, blank=True, max_length=100)
    permission_level = models.CharField(
        max_length=2, choices=OrganizationMemberPermission.choices)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.permission_level


class Organization(models.Model):
    class OrgType(models.TextChoices):
        STARTUP = 'st', _('Startup')
        COMPANY = 'cm', _('Company')
        HR_FIRM = 'hr', _('Hr Firm')
        RECRUITMENT_FIRM = 'rf', _('Recuitment Firm')

    org_id = models.UUIDField(default=uuid.uuid4, editable=False)
    contacts = models.ManyToManyField(OrganizationContact, blank=True)
    name = models.CharField(max_length=100, unique=True)
    cover_pic = models.ImageField(
        upload_to='uploads/% Y/% m/% d/', blank=True, null=True)
    org_type = models.CharField(choices=OrgType.choices, max_length=2)
    org_status = models.ForeignKey(
        OrganizationStatus, on_delete=models.CASCADE, blank=True, null=True)
    pipeline_template = models.CharField(
        choices=OrgType.choices, max_length=2, blank=True, null=True,
        help_text="Default pipeline template to be created will be based on org type")
    verified = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(OrganizationMember, blank=True)
    employees_count = models.IntegerField(null=True, blank=True)
    subdomain = models.CharField(max_length=200, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
