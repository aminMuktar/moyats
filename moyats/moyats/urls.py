from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from graphql_playground.views import GraphQLPlaygroundView
from graphql_jwt.decorators import jwt_cookie
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_file_upload.django import FileUploadGraphQLView


class HomePageView(TemplateView):
    template_name: str = "home.html"




urlpatterns = [
    path('graphql/',  csrf_exempt(
        jwt_cookie(FileUploadGraphQLView.as_view(graphiql=True)))),
    path('playground/', GraphQLPlaygroundView.as_view(endpoint="/graphql/")),
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),

    url(r'^.*$', HomePageView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
