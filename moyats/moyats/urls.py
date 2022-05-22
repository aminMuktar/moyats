from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from graphql_playground.views import GraphQLPlaygroundView
from graphene_file_upload.django import FileUploadGraphQLView
from graphql_jwt.decorators import jwt_cookie


class GqlView(FileUploadGraphQLView, LoginRequiredMixin):
    pass


urlpatterns = [
    path('graphql/',  csrf_exempt(jwt_cookie(GqlView.as_view(graphiql=True)))),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
    path('playground/', GraphQLPlaygroundView.as_view(endpoint="/graphql/")),
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
