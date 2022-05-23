from django.db import models
from emails.models import CoreEmail
from candidates.models import Candidate
from organizations.models import Organization
from organizations.models import Color
from django.utils.translation import gettext_lazy as _


class Trigger(models.Model):
    class TriggerAction(models.TextChoices):
        SEND_EMAIL = 'se', _('Send Email')
        SUBMIT_TO_CLIENT = 'sc', _('Submit To Client')
        SEND_TELEGRAM_MESSAGE = 'st', _('Send Telegram Message')
        ADD_CALENDAR = 'ac', _('Add Calendar Entry')
        WEBHOOK = 'wh', _('Send Webhook')

    class TriggerRequirements(models.TextChoices):
        REQUIRED = 'rq', _('Required')
        DEFAULT_ON_OPTIONAL = 'do', _('Optional, on by Default')
        DEFAULT_OFF_OPTIONAL = 'df', _('Optional, off by Default')

    aciton = models.CharField(
        max_length=2, choices=TriggerAction.choices, default=TriggerAction.SEND_EMAIL)
    description = models.TextField(null=True, blank=True)
    required_type = models.CharField(
        max_length=2, choices=TriggerRequirements.choices, default=TriggerRequirements.DEFAULT_OFF_OPTIONAL)
    email_composition_details = models.ForeignKey(CoreEmail, on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.aciton


class PipelineStatus(models.Model):
    status_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    default = models.BooleanField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.status_name


class PipelineSetup(models.Model):
    title = models.CharField(max_length=100)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    status = models.ForeignKey(
        PipelineStatus, related_name="status", on_delete=models.CASCADE)
    mapping_status = models.ForeignKey(
        PipelineStatus, related_name="mapping_status", on_delete=models.CASCADE)
    prerequisite_status = models.ManyToManyField(
        PipelineStatus, related_name="prerequisite_status", null=True, blank=True)
    triggers = models.ManyToManyField(Trigger, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class PipelineWorkflow(models.Model):
    candidates = models.ManyToManyField(Candidate, blank=True)
    pipeline_setup = models.ForeignKey(PipelineSetup, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.pipeline_setup.title