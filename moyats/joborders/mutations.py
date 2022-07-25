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
            start_date=input.start_date,
            max_rate=input.max_rate,
            min_rate=input.min_rate,
            position_type=input.type,
            category=category.first(),
            openings=input.openings,
            remaining_openings=input.openings,
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
        jorder.update(job_order_status=stat.first())
        return UpdateJobOrderStatus(response=True)


class UpdateJobOrderPrimary(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        input = JobOrderPrimaryInput(required=True)
        joborder = graphene.UUID()

    @login_required
    def mutate(self, info, input: JobOrderPrimaryInput, joborder, **kwargs):
        jborder = JobOrder.objects.filter(
            joborder_id=joborder
        )
        if not jborder.exists():
            raise Exception("Joborder not found")

        recruiter = OrganizationMember.objects.filter(
            org_member_id=input.recruiter
        )
        if not recruiter.exists():
            raise Exception("Recruiter not found")

        loc = None
        location = Address.objects.filter(
            country=input.country, city=input.city)
        if not location.exists():
            loc = Address.objects.create(
                country=input.country, city=input.city)
        else:
            loc = location.first()
        print(loc,"D"*30)
        jorder_details = jborder.first().job_detail
        JobDetail.objects.filter(id=jorder_details.id).update(
            location=loc,
            recruiter=recruiter.first())
        return UpdateJobOrderPrimary(response=True)


class AddJobOrder(graphene.Mutation):
    response = graphene.Field(JobOrderType)

    class Arguments:
        input = JobOrderInputs(required=True)

    @login_required
    def mutate(self, info, input: JobOrderInputs):
        org = info.context.user.organizations.first()

        recruiter = OrganizationMember.objects.filter(
            org_member_id=input.recruiter
        )

        order_type = JobOrderTypes.objects.filter(
            id=input.order_type
        )
        if not recruiter.exists():
            raise Exception("Recruiter not found")

        if not order_type.exists():
            raise Exception("Order Type not found")

        category = JobOrderCategory.objects.filter(
            id=input.category
        )

        if not category.exists():
            raise Exception("Category Does not exist")

        # Test location
        location = Address.objects.create(
            country=input.country,
            city=input.city,
        )

        job_details = JobDetail.objects.create(
            title=input.title,
            location=location,
            position_type=input.position_type,
            recruiter=recruiter.first(),
            start_date=input.start_date,
            salary=input.salary,
            max_rate=input.max_rate,
            min_rate=input.min_rate,
            duration=input.duration,
            order_type=order_type.first(),
            openings=input.openings,
            remaining_openings=input.openings,
            category=category.first(),
        )

        job_order_status = JoborderStatus.objects.filter(
            id=input.status
        )

        if not job_order_status.exists():
            raise Exception("Job order status Does not exist")

        company = Company.objects.filter(
            company_id=input.company
        )

        if not company.exists():
            raise Exception("Company Does not exist")

        # use defauly pipeline workflow for joborders if pipeline is dead
        pipeline_workflow = None
        if input.pipeline_workflow:
            pipeline_workflow = PipelineWorkflow.objects.filter(
                title=input.pipeline_workflow
            )
        else:
            pipeline_workflow = PipelineWorkflow.objects.filter(
                organization=org
            )

        if not pipeline_workflow.exists():
            raise Exception("Pipeline Does not exist")


        add_job_order = JobOrder.objects.create(
            notes=input.notes,
            description=input.description,
            job_detail=job_details,
            job_order_status=job_order_status.first(),
            organization=org,
            company=company.first(),
            pipeline_workflow=pipeline_workflow.first()
        )

        for app in input.applications:
            ap = Application.objects.filter(application_id=app)
            if not ap.exists():
                raise Exception("Application not found")
            add_job_order.applications.add(ap.first())

        return AddJobOrder(response=add_job_order)
