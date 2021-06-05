from django.conf import settings
from django.urls import path

from django_github_oauth.views import GithubOAuthLoginView

urlpatterns = [
    path('', GithubOAuthLoginView.as_view()),
]
