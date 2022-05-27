import graphene


class NewUserInput(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    middle_name = graphene.String()
    phone_number = graphene.String()
    email = graphene.String(required=True)
    password = graphene.String(required=True)


class SocialRegistrationInput(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    source = graphene.String()
    email = graphene.String()
    photo_url = graphene.String()
    access_token = graphene.String()
