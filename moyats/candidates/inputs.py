import graphene


class SocialMediaInput(graphene.InputObjectType):
    link = graphene.String()


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
