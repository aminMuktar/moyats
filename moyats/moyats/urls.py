from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from graphql_playground.views import GraphQLPlaygroundView
from graphene_file_upload.django import FileUploadGraphQLView

class GqlView(FileUploadGraphQLView, LoginRequiredMixin):
    pass

urlpatterns = [
    path('graphql/',  csrf_exempt(GqlView.as_view(graphiql=True))),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
    path('playground/', GraphQLPlaygroundView.as_view(endpoint="/graphql/")),
    path('admin/', admin.site.urls),
]
