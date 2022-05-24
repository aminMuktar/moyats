import graphene


class NewUserInput(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    middle_name = graphene.String()
    phone_number = graphene.String()
    email = graphene.String(required=True)
    password = graphene.String(required=True)
    company_title = graphene.String(required=True)
    company_type = graphene.String(required=True)
    subdomain = graphene.String(required=True)
    employees_count = graphene.Int(required=True)