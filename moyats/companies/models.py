import uuid
from django.db import models
from core.models import Color
from accounts.models import BaseContact, Address
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation


class CompanyStatus(models.Model):
    name = models.CharField(max_length=300)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    default = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Company(models.Model):
    class OrgType(models.TextChoices):
        STARTUP = 'st', _('Startup')
        COMPANY = 'cm', _('Company')
        HR_FIRM = 'hr', _('Hr Firm')
        RECRUITMENT_FIRM = 'rf', _('Recuitment Firm')

    company_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, unique=True)
    website = models.URLField(null=True, blank=True, help_text="Optional field for companies websites")
    phones = models.ForeignKey(
        BaseContact, on_delete=models.CASCADE, null=True)
    company_status = models.ForeignKey(
        CompanyStatus, on_delete=models.CASCADE, blank=True, null=True)
    verified = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    organization = models.ForeignKey(
        "organizations.Organization", on_delete=models.CASCADE, null=True)
    activity = GenericRelation("core.Activity")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class CompanyContactStatus(models.Model):
    name = models.CharField(max_length=100)
    color = models.ForeignKey("core.Color", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class CompanyContact(models.Model):
    company_contact_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=200, null=True)
    phones = models.ForeignKey(
        BaseContact, on_delete=models.CASCADE, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    reachable = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    contact_reports_to = models.ForeignKey(
        "self", related_name="reports_to", null=True, blank=True, on_delete=models.CASCADE)
    status = models.ForeignKey(
        CompanyContactStatus, on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email
