import graphene


class OrgSetupInput(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    middle_name = graphene.String()
    phone_number = graphene.String()
    org_type = graphene.String()
    org_name = graphene.String()
    subdomain = graphene.String()