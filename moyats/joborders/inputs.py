import graphene


class JobOrderPrimaryInput(graphene.InputObjectType):
    title = graphene.String()
    city = graphene.String()
    country = graphene.String()
    recruiter = graphene.UUID()


class JobOrderDetailInput(graphene.InputObjectType):
    salary = graphene.String()
    start_date = graphene.Date()
    duration = graphene.String()
    max_rate = graphene.String()
    min_rate = graphene.String()
    type = graphene.String()
    category = graphene.Int()
    publish = graphene.Boolean()
    openings = graphene.Int()
    status = graphene.String()


class JobOrderInputs(graphene.InputObjectType):
    notes = graphene.String()
    description = graphene.String()
    title = graphene.String()
    city = graphene.String()
    state = graphene.String()
    recruiter = graphene.String()
    country = graphene.String()
    position_type = graphene.String()
    start_date = graphene.Date()
    salary = graphene.String()
    max_rate = graphene.String()
    min_rate = graphene.String()
    duration = graphene.String()
    openings = graphene.String()
    order_type = graphene.String()
    category = graphene.String()
    status = graphene.String()
    company = graphene.String()
    contact = graphene.String()
    applications = graphene.List(graphene.String)
    pipeline_workflow = graphene.String()
