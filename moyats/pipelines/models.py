import uuid
from django.db import models
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

    trigger_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    aciton = models.CharField(
        max_length=2, choices=TriggerAction.choices, default=TriggerAction.SEND_EMAIL)
    description = models.TextField(null=True, blank=True)
    required_type = models.CharField(
        max_length=2, choices=TriggerRequirements.choices, default=TriggerRequirements.DEFAULT_OFF_OPTIONAL)
    email_composition_details = models.ForeignKey("emails.CoreEmail", on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.aciton


class PipelineStatus(models.Model):
    status_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    default = models.BooleanField()
    organization = models.ForeignKey("organizations.Organization", on_delete=models.CASCADE, null=True)
    color = models.ForeignKey("core.Color", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.status_name

class PipelineSetup(models.Model):
    pipeline_setup_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    step = models.BigIntegerField(null=True)
    color = models.ForeignKey("core.Color", on_delete=models.CASCADE)
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
        return f"{self.step}-{self.status.status_name}"


class PipelineWorkflow(models.Model):
    pipeline_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100, null=True)
    candidates = models.ManyToManyField("candidates.Candidate", blank=True)
    pipeline_setups = models.ManyToManyField(PipelineSetup)
    default = models.BooleanField(default=False, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title