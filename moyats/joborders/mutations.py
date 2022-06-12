import graphene
from accounts.models import Address, BaseUser
from companies.models import Company
from pipelines.models import PipelineWorkflow

from organizations.models import Organization, OrganizationMember
from .types import JobOrderType
from .inputs import JobOrderInputs
from .models import JobDetail, JobOrder, JobOrderCategory, JobOrderTypes, JoborderStatus
from graphql_jwt.decorators import login_required

# Test run


class JobOrderMutation(graphene.Mutation):
    response = graphene.Field(JobOrderType)

    class Arguments:
        input = JobOrderInputs(required=True)

    @login_required
    def mutate(self, info, input: JobOrderInputs):

        recruiter = OrganizationMember.objects.filter(
            user=info.context.user.id
        )

        order_type = JobOrderTypes.objects.filter(
            type_name=input.order_type
        )

        if not order_type.exists():
            raise Exception("Order Type not found")

        category = JobOrderCategory.objects.filter(
            category_name=input.catagory
        )

        if not category.exists():
            raise Exception("Category Does not exist")

        # Test location
        location = Address.objects.filter(
            country=input.location
        )

        if not location.exists():
            raise Exception("Location not found")

        job_details = JobDetail.objects.create(
            title=input.title,
            location=location.first(),
            position_type=input.position_type,
            recruiter=recruiter.first(),
            start_date=input.start_date,
            salary=input.salary,
            max_rate=input.max_rate,
            duration=input.duration,
            order_type=order_type.first(),
            openings=input.openings,
            remaining_openings=input.remaining_openings,
            publish=input.publish,
            category=category.first(),
            hot=input.hot
        )

        job_order_status = JoborderStatus.objects.filter(
            status_name=input.job_order_status
        )

        if not job_order_status.exists():
            raise Exception("Job order status Does not exist")

        company = Company.objects.filter(
            name=input.company
        )

        if not company.exists():
            raise Exception("Company Does not exist")

        pipeline_workflow = PipelineWorkflow.objects.filter(
            title=input.pipeline_workflow
        )

        if not pipeline_workflow.exists():
            raise Exception("Pipeline Does not exist")

        organization = Organization.objects.filter(
            name=input.organization
        )

        if not organization.exists():
            raise Exception("Organization Does not exist")

        add_job_order = JobOrder.objects.create(
            notes=input.notes,
            description=input.desctiption,
            job_detail=job_details,
            job_order_status=job_order_status.first(),
            organization=organization.first(),
            company=company.first(),
            pipeline_workflow=pipeline_workflow.first()
        )

        return JobOrderMutation(response=add_job_order)