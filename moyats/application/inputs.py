import graphene


class ApplicationQuestionInput(graphene.InputObjectType):
    title = graphene.String()
    comment = graphene.String()
    required = graphene.Boolean()
    save_to = graphene.String()
