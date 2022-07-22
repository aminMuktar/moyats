import graphene

from candidates.inputs import SocialMediaInput


class ContactPhonesInput(graphene.InputObjectType):
    cell_phone = graphene.String(required=True)
    home_phone = graphene.String(required=False)
    work_phone = graphene.String(required=False)

class NameInput(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()

class ContactPrimaryInfoUpdateInput(graphene.InputObjectType):
    name = graphene.Field(NameInput)
    contact = graphene.UUID()
    phones = graphene.Field(ContactPhonesInput)
    address = graphene.String()

class CompanyPrimaryInfoUpdateInput(graphene.InputObjectType):
    name = graphene.String()
    phones = graphene.Field(ContactPhonesInput)
    city = graphene.String()
    country = graphene.String()
    state = graphene.String()
    website = graphene.String()
    company = graphene.String()
    # social_medias = graphene.List(SocialMediaInput)


class CompanyInput(graphene.InputObjectType):
    name = graphene.String()
    phones = graphene.Field(ContactPhonesInput)
    city = graphene.String()
    country = graphene.String()
    state = graphene.String()
    website = graphene.String()
    key_technologies = graphene.String()
    departments = graphene.String()
    notes = graphene.String()