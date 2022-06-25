import graphene


class JobOrderPrimaryInput(graphene.InputObjectType):
    title = graphene.String()
    location = graphene.Int()
    recruiter = graphene.Int()


class JobOrderDetailInput(graphene.InputObjectType):
    salary = graphene.String()
    duration = graphene.String()
    max_rate = graphene.String()
    min_rate = graphene.String()
    type = graphene.String()
    category = graphene.Int()
    publish = graphene.Boolean()
    openings = graphene.Int()
    remaining_openings = graphene.Int()
    status = graphene.String()


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
