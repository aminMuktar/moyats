import graphene
from .types import ApplicationQuestionType
from .enums import SaveApplicationDetailTypes
from graphql_jwt.decorators import login_required
from .models import Application, ApplicationQuestion
from core.types import EnumType


class ApplicationQuery(graphene.ObjectType):
    application_questions = graphene.List(
        ApplicationQuestionType, application=graphene.String())
    save_application_detail_types = graphene.List(EnumType)

    @login_required
    def resolve_save_application_detail_types(self, info, **kwargs):
        pos_types = [{'id': year[0], 'label': year[1]}
                     for year in SaveApplicationDetailTypes.choices]
        return pos_types

    @login_required
    def resolve_application_questions(self, info, application, **kwargs):
        org = info.context.user.organizations.first()
        applications = Application.objects.filter(
            organization=org, application_id=application)
        if not applications.exists():
            raise Exception("Application not found")
        questions = ApplicationQuestion.objects.filter(
            application=applications.first()
        )
        return questions
