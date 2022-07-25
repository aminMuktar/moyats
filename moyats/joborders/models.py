from statistics import mode
import uuid
from django.db import models
from accounts.models import Address
from companies.models import Company
from core.models import Attachment
from .enums import PositionTypes


class JobOrderTypes(models.Model):
    type_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.type_name


class JobOrderCategory(models.Model):
    category_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.category_name


class JobDetail(models.Model):
    title = models.CharField(max_length=200)
    location = models.ForeignKey(Address, on_delete=models.CASCADE)
    position_type = models.CharField(
        choices=PositionTypes.choices, max_length=2)
    recruiter = models.ForeignKey(
        "organizations.OrganizationMember", on_delete=models.CASCADE)
    start_date = models.DateField()
    salary = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    max_rate = models.CharField(max_length=100)
    min_rate = models.CharField(max_length=100, null=True)
    order_type = models.ForeignKey(JobOrderTypes, on_delete=models.CASCADE)
    category = models.ForeignKey(JobOrderCategory, on_delete=models.CASCADE)
    openings = models.BigIntegerField()
    remaining_openings = models.BigIntegerField()
    hot = models.BooleanField(default=False)
    publish = models.BooleanField(
        default=True, help_text="publish job order on publish status change")
    updated_At = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class JoborderStatus(models.Model):
    status_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    default = models.BooleanField()
    color = models.ForeignKey("core.Color", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.status_name


class JobOrder(models.Model):
    joborder_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    notes = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    job_detail = models.ForeignKey(JobDetail, on_delete=models.CASCADE)
    applications = models.ManyToManyField(
        "application.Application", blank=True, null=True)
    job_order_status = models.ForeignKey(
        JoborderStatus, on_delete=models.CASCADE, null=True)
    attachments = models.ManyToManyField(Attachment, blank=True)
    organization = models.ForeignKey(
        "organizations.Organization", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    pipeline_workflow = models.ForeignKey(
        "pipelines.PipelineWorkflow", on_delete=models.CASCADE)
    updated_At = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.job_detail.title


class JobOrderApplicant(models.Model):
    joborder_applicant_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    candidate = models.ForeignKey(
        "candidates.Candidate", on_delete=models.CASCADE, null=True)
    joborder = models.ForeignKey(
        JobOrder, on_delete=models.CASCADE, null=True, blank=True)
    status = models.ForeignKey(
        "pipelines.PipelineStatus", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.candidate.candidate_profile.first_name
