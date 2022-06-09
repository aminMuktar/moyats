import uuid
from django.db import models
from accounts.models import BaseUser
from organizations.models import Organization
from django.utils.translation import gettext_lazy as _


class Application(models.Model):
    application_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=300)
    header = models.TextField()
    updated_At = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description


class ApplicationQuestion(models.Model):
    class SaveApplicationDetailTypes(models.TextChoices):
        APPLICATION_ONLY = 'ao', _('Application Only')
        RESUME = 'rs', _('Resume')
        FIRST_NAME = 'fn', _('First Name')
        MIDDLE_NAME = 'mn', _('Middle Name')
        LAST_NAME = 'ln', _('Last Name')
        PHONE_HOME = 'ph', _('Home Phone')
        PHONE_MOBILE = 'pm', _('Mobile Phone')
        PHONE_WORK = 'pw', _('Work Phone')
        ADDRESS = 'ad', _('Address')
        CITY = 'ct', _('City')
        STATE = 'st', _('State')
        ZIP_CODE = 'zc', _('Zip Code')
        SOURCE = 'sr', _('Source')
        KEY_SKILLS = 'ks', _('Key Skills')
        CURRENT_EMPLOYEER = 'ce', _('Current Employeer')
        EMAIL = 'em', _('Email')
        DESIRED_PAY = 'dp', _('Desired Pay')
        CURRENT_PAY = 'cp', _('Current Pay')
        COUNTRY = 'cn', _('Country')
        WORK_HISTORY = 'wh', _('Work History')
        SOCIAL_MEDIA = 'sm', _('Social Media')
    application = models.ForeignKey(
        Application, on_delete=models.CASCADE, null=True)
    question_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    field_title = models.CharField(
        max_length=300, help_text="Keep it simple. Put additional information in the comment.")
    comment = models.TextField(help_text="Hint or comment on a field")
    save_to = models.CharField(
        max_length=2, choices=SaveApplicationDetailTypes.choices,
        default=SaveApplicationDetailTypes.APPLICATION_ONLY,
        help_text="Information in the result will be saved to one of these fields upon recival")
    required = models.BooleanField(default=False)
    updated_At = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.field_title


class ScoreCardItem(models.Model):
    sc_item_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name


class ScoreCardReivewCategory(models.Model):
    sc_cat_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    items = models.ManyToManyField(ScoreCardItem)

    def __str__(self) -> str:
        return str(self.sc_cat_id)


class ScoreCard(models.Model):
    sc_cat_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    category = models.ManyToManyField(
        ScoreCardReivewCategory)

    def __str__(self) -> str:
        return str(self.sc_cat_id)


class ReviewStep(models.Model):
    class ReviewStepTypes(models.TextChoices):
        SCORE_CARD = 'sc', _('Score Card')
        APPROVAL_ONLY = 'ao', _('ApprovalOnly')

    class ReviewApprovalTypes(models.TextChoices):
        SCORE_CARD = 'on', _('One')
        APPROVAL_ONLY = 'al', _('All')

    review_step_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=500)
    reviewers = models.ManyToManyField(BaseUser)
    type = models.CharField(max_length=2, choices=ReviewStepTypes.choices)
    approval = models.CharField(max_length=2, choices=ReviewApprovalTypes.choices,
                                help_text="Require approval from one or all reviewers")
    approval_status = models.ForeignKey(
        "pipelines.PipelineStatus", on_delete=models.CASCADE, related_name="approval_status",
        help_text="Move candidate to this status if approved by the reviewer")

    declined_status = models.ForeignKey(
        "pipelines.PipelineStatus", on_delete=models.CASCADE, related_name="declined_status",
        help_text="Move candidate to this status if declined by the reviewer")

    purpose = models.TextField(
        help_text="Describe the purpose of this step. Visible to all reviewers.")
    key_questions = models.ManyToManyField(ScoreCardItem)

    def __str__(self) -> str:
        return self.title


class ReviewStepSet(models.Model):
    review_step_set_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    status = models.ForeignKey(
        "pipelines.PipelineStatus", on_delete=models.CASCADE)
    step = models.ForeignKey(ReviewStep, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.review_step_set_id)
