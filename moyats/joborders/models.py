from django.db import models
from accounts.models import Address
from django.utils.translation import gettext_lazy as _
from organizations.models import Organization, OrganizationMember

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
    class PositionTypes(models.TextChoices):
        REMOTE = 'rm', _('Remote')
        FULL_TIME = 'fl', _('Full Time')
        PART_TIME = 'pt', _('Part Time')
        FREELANCE = 'fr', _('Freelance')
        WITH_RELOCATION = 'rl', _('With Relocation')

    title = models.CharField(max_length=200)
    location = models.ForeignKey(Address, on_delete=models.CASCADE)
    position_type = models.CharField(choices=PositionTypes.choices, max_length=2)
    recruiter = models.ForeignKey(OrganizationMember, on_delete=models.CASCADE)
    start_date = models.DateField()
    salary = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    max_rate = models.CharField(max_length=100)
    order_type = models.ForeignKey(JobOrderTypes, on_delete=models.CASCADE)
    category = models.ForeignKey(JobOrderCategory, on_delete=models.CASCADE)
    openings = models.BigIntegerField()
    remaining_openings = models.BigIntegerField()
    hot = models.BooleanField()
    publish = models.BooleanField(default=True, help_text="publish job order on publish status change")
    updated_At = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class JobOrder(models.Model):
    notes = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    job_detail = models.ForeignKey(JobDetail, on_delete=models.CASCADE)
    # application
    job_order_status = models.ForeignKey("pipelines.PipelineStatus", on_delete=models.CASCADE, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    pipeline_workflow = models.ForeignKey("pipelines.PipelineWorkflow", on_delete=models.CASCADE)
    updated_At = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.job_detail.title