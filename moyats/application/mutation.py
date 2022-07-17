import graphene
from .inputs import ApplicationQuestionInput
from graphql_jwt.decorators import login_required
from .models import ApplicationQuestion, Application


class SaveApplicationQuestion(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        input = ApplicationQuestionInput(required=True)
        application = graphene.String()

    @login_required
    def mutate(self, info, input, application, **kwargs):
        applications = Application.objects.filter(application_id=application)
        if not applications.exists():
            raise Exception("application not found")
        ApplicationQuestion.objects.create(
            application=applications.first(),
            field_title=input.title,
            comment=input.comment,
            save_to=input.save_to,
            required=input.required
        )
        return SaveApplicationQuestion(response=True)
