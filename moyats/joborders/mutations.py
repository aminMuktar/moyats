import graphene
from .types import JobOrderType
from accounts.models import Address
from companies.models import Company
from application.models import Application
from pipelines.models import PipelineWorkflow
from graphene_file_upload.scalars import Upload
from organizations.models import Organization, OrganizationMember
from .inputs import JobOrderDetailInput, JobOrderInputs, JobOrderPrimaryInput
from .models import JobDetail, JobOrder, JobOrderCategory, JobOrderTypes, JoborderStatus
from graphql_jwt.decorators import login_required


class UpdateJobOrderCompany(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        company = graphene.UUID()
        joborder = graphene.UUID()

    @login_required
    def mutate(self, info, company, joborder, **kwargs):
        jorder = JobOrder.objects.filter(joborder_id=joborder)
        if not jorder.exists():
            raise Exception("joborder not found")
        cmp = Company.objects.filter(company_id=company)
        if not cmp.exists():
            raise Exception("Company not found")
        jorder.update(company=cmp.first())
        return UpdateJobOrderCompany(response=True)


class AddJobOrderAttachments(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        file = Upload(required=True)
        joborder = graphene.String()
        filename = graphene.String()
        is_resume = graphene.Boolean()

    @login_required
    def mutate(self, info, file, joborder, filename, is_resume, **kwargs):
        jorder = JobOrder.objects.filter(joborder_id=joborder)
        if not jorder.exists():
            raise Exception("joborder not found")
        jorder.first().attachments.create(file=file, filename=filename, is_resume=is_resume)
        return AddJobOrderAttachments(response=True)


class UpdateJoborderApplication(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        application = graphene.UUID()
        joborder = graphene.UUID()

    @login_required
    def mutate(self, info, application, joborder, **kwargs):
        jorder = JobOrder.objects.filter(joborder_id=joborder)
        if not jorder.exists():
            raise Exception("Joborder not found")
        app = Application.objects.filter(application_id=application)
        if not app.exists():
            raise Exception("Application not found")
        jorder.update(application=app.first())
        return UpdateJoborderNotes(response=True)


class UpdateJoborderNotes(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        notes = graphene.String()
        joborder = graphene.String()

    @login_required
    def mutate(self, info, notes, joborder, **kwargs):
        jorder = JobOrder.objects.filter(joborder_id=joborder)
        if not jorder.exists():
            raise Exception("Joborder not found")
        jorder.update(notes=notes)
        return UpdateJoborderNotes(response=True)


class UpdateJoborderDescription(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        description = graphene.String()
        joborder = graphene.String()

    @login_required
    def mutate(self, info, description, joborder, **kwargs):
        jorder = JobOrder.objects.filter(joborder_id=joborder)
        if not jorder.exists():
            raise Exception("Joborder not found")
        jorder.update(description=description)
        return UpdateJoborderDescription(response=True)


class UpdateJobOrderDetails(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        input = JobOrderDetailInput()
        joborder = graphene.String()

    @login_required
    def mutate(self, info, input: JobOrderDetailInput, joborder, **kwargs):
        jorder = JobOrder.objects.filter(
            joborder_id=joborder
        )
        if not jorder.exists():
            raise Exception("Joborder not found")
        category = JobOrderCategory.objects.filter(
            id=input.category
        )
        if not category.exists():
            raise Exception("Category not found")

        jorder_detail = JobDetail.objects.filter(
            id=jorder.first().job_detail.id)
        jorder_detail.update(
            salary=input.salary,
            duration=input.duration,
            max_rate=input.max_rate,
            min_rate=input.min_rate,
            position_type=input.type,
            category=category.first(),
            openings=input.openings,
            remaining_openings=input.remaining_openings,
            publish=input.publish
        )
        return UpdateJobOrderDetails(response=True)


class UpdateJobOrderStatus(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        status = graphene.Int()
        joborder = graphene.String()

    @login_required
    def mutate(self, info, status, joborder, **kwargs):
        jorder = JobOrder.objects.filter(joborder_id=joborder)
        if not jorder.exists():
            raise Exception("Joborder not found")

        stat = JoborderStatus.objects.filter(
            id=status
        )
        if not stat.exists():
            raise Exception("Status not found")
        JobOrder.objects.update(job_order_status=stat.first())
        return UpdateJobOrderStatus(response=True)


class UpdateJobOrderPrimary(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        input = JobOrderPrimaryInput(required=True)
        joborder = graphene.String()

    @login_required
    def mutate(self, info, input, joborder, **kwargs):
        jborder = JobOrder.objects.filter(
            joborder_id=joborder
        )
        if not jborder.exists():
            raise Exception("Joborder not found")

        recruiter = OrganizationMember.objects.filter(
            user=input.recruiter
        )
        location = Address.objects.filter(id=input.location)
        if not recruiter.exists():
            raise Exception("Recruiter not found")
        jorder_details = jborder.first().job_detail
        JobDetail.objects.filter(id=jorder_details.id).update(
            title=input.title, location=location.first(),
            recruiter=recruiter.first())
        return UpdateJobOrderPrimary(response=True)


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
