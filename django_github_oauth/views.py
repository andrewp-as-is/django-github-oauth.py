from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic.base import View
import requests

from .models import User
from .oauth_client import OAuthClient

class GithubOAuthLoginView(View):
    def dispatch(self, request, *args, **kwargs):
        client = OAuthClient(request)
        return redirect(client.get_redirect_url())

class GithubOAuthCallbackView(View):
    def dispatch(self, request, *args, **kwargs):
        client = OAuthClient(self.request)
        self.token = client.get_access_token(request.GET['code'])
        return super(GithubOAuthCallbackView, self).dispatch(request, *args, **kwargs)

    def get(self,request, *args, **kwargs):
        headers = {'Authorization': 'token %s' % self.token}
        r = requests.get('https://api.github.com/user', headers=headers)
        data = r.json()
        defaults = dict(login=data['login'],token=self.token)
        user, created = User.objects.update_or_create(defaults,id=data['id'])
        login(request, user, backend='django_passwordless_auth.backend.PasswordlessAuthBackend')
        return redirect(settings.LOGIN_REDIRECT_URL if settings.LOGIN_REDIRECT_URL else '/')
