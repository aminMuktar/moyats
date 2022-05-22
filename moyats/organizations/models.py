from django.db import models
from django.utils.translation import gettext_lazy as _


class Color(models.Model):
    hex = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.hex


class OrganizationStatus(models.Model):
    name = models.CharField(max_length=300)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    default = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class OrganizationContact(models.Model):
    phones = models.ForeignKey("accounts.BaseContact", on_delete=models.CASCADE)
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

    user = models.ForeignKey("accounts.BaseUser", on_delete=models.CASCADE)
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

    contacts = models.ManyToManyField(OrganizationContact, blank=True)
    name = models.CharField(max_length=100)
    cover_pic = models.ImageField(upload_to='uploads/% Y/% m/% d/')
    org_type = models.CharField(choices=OrgType.choices, max_length=2)
    org_status = models.ForeignKey(
        OrganizationStatus, on_delete=models.CASCADE)
    pipeline_template = models.CharField(
        choices=OrgType.choices, max_length=2, help_text="Default pipeline template to be created will be based on org type")
    verified = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(OrganizationMember, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
