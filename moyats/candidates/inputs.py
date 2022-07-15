import graphene


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
    # social_medias = graphene.List(SocialMediaInput)
    country = graphene.String()
    city = graphene.String()


class CandidateDetailInput(graphene.InputObjectType):
    source = graphene.String()
    key_skills = graphene.String()
    current_employeer = graphene.String()
    date_available = graphene.String()
    current_pay = graphene.String()
    desired_pay = graphene.String()


class CandidateInput(graphene.InputObjectType):
    firstName = graphene.String()
    middleName = graphene.String()
    lastName = graphene.String()
    email = graphene.String()
    cell_phone = graphene.String()
    home_phone = graphene.String()
    work_phone = graphene.String()
    socialMedias = graphene.List(SocialMediaInput)
    country = graphene.String()
    city = graphene.String()
    source = graphene.String()
    keySkills = graphene.String()
    currentEmployeer = graphene.String()
    notes = graphene.String()
    dateAvailable = graphene.String()
    currentPay = graphene.String()
    desiredPay = graphene.String()
    bestContactTime = graphene.String()
    website = graphene.String()
    qualifications = graphene.String()


class CandidateWorkHistoryInput(graphene.InputObjectType):
    title = graphene.String()
    employeer = graphene.String()
    currently_working = graphene.Boolean()
    start_date = graphene.String()
    end_date = graphene.String()
    leaving_reason = graphene.String()
