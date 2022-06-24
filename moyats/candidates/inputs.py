import graphene


class CandidateDetailInput(graphene.InputObjectType):
    pass


class SocialMediaInput(graphene.InputObjectType):
    link = graphene.String()
    type = graphene.String()


class CandidateProfileInput(graphene.InputObjectType):
    first_name = graphene.String()
    middle_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()


class PhonenumberInput(graphene.InputObjectType):
    cell_number = graphene.String()
    work_number = graphene.String()
    home_number = graphene.String()


class CandidatePrimaryInput(graphene.InputObjectType):
    candidate_profile = graphene.Field(CandidateProfileInput)
    phones = graphene.Field(PhonenumberInput)
    social_medias = graphene.List(SocialMediaInput)
    address = graphene.Int()


class CandidateInput(graphene.InputObjectType):
    firstName = graphene.String()
    middleName = graphene.String()
    lastName = graphene.String()
    email = graphene.String()
    organization = graphene.String()
    phone = graphene.String()
    socialMedias = graphene.List(SocialMediaInput)
    country = graphene.String()
    city = graphene.String()
    zipCode = graphene.Int()
    source = graphene.String()
    keySkills = graphene.String()
    currentEmployeer = graphene.String()
    dateAvailable = graphene.String()
    currentPay = graphene.String()
    desiredPay = graphene.String()
    bestContactTime = graphene.String()
    website = graphene.String()
    qualifications = graphene.String()
    attachments = graphene.String()
