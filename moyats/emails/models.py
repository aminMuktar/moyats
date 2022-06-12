import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class EmailReport(models.Model):
    class EmailStatus(models.TextChoices):
        OPENED = 'op', _('Opened')
        CLICKED = 'cl', _('Clicked')
        BOUNCED = 'bo', _('Bounced')
        UNSUBSCRIBED = 'us', _('Unsubscribed')
        MARKED_SPAM = 'ms', _('Marked Spam')

    email_report_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    opens = models.BigIntegerField(default=0)
    clicks = models.BigIntegerField(default=0)
    bounces = models.BigIntegerField(default=0)
    unsubscribes = models.BigIntegerField(default=0)
    spam = models.BigIntegerField(default=0)
    open_rate = models.CharField(max_length=200)
    click_rate = models.CharField(max_length=200)
    status = models.CharField(max_length=2, choices=EmailStatus.choices)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.status

class EmailRecipient(models.Model):
    class EmailRecipientType(models.TextChoices):
        CONTACT = 'co', _('Contact')
        CANDIDATE = 'ca', _('Candidate')
        CUSTOM_DETAIL = 'cd', _('Custom Detail')

    email_recipient_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    type = models.CharField(choices=EmailRecipientType.choices, max_length=2)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    report = models.ForeignKey(
        EmailReport, on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name

class CoreEmail(models.Model):
    email_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    regarding = models.ForeignKey("joborders.JobOrder", on_delete=models.CASCADE)
    recipient = models.ForeignKey(EmailRecipient, on_delete=models.CASCADE)
    subject = models.TextField()
    body = models.TextField()
    signiture = models.TextField()
    schedule = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.subject