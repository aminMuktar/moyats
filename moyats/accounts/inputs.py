import graphene


class NewUserInput(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    middle_name = graphene.String()
    phone_number = graphene.String()
    password = graphene.String(required=True)


class SocialRegistrationInput(graphene.InputObjectType):
    source = graphene.String()
    email = graphene.String()
    photo_url = graphene.String()
    access_token = graphene.String()
