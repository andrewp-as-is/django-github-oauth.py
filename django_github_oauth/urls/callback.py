from django.urls import path

from django_github_oauth.views import GithubOAuthCallbackView

urlpatterns = [
    path('', GithubOAuthCallbackView.as_view(),name='callback'),
]
