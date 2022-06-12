import graphene


class JobOrderInputs(graphene.InputObjectType):
    notes = graphene.String()
    desctiption = graphene.String()
    title = graphene.String()
    location = graphene.String()
    recruiter = graphene.String()
    position_type = graphene.String()
    start_date = graphene.Date()
    salary = graphene.String()
    max_rate = graphene.String()
    duration = graphene.Date()
    openings = graphene.String()
    order_type = graphene.String()
    catagory = graphene.String()
    remaining_openings = graphene.String()
    job_order_status = graphene.String()
    publish = graphene.String()
    organization = graphene.String()
    company = graphene.String()
    pipeline_workflow = graphene.String()
    hot = graphene.Boolean()