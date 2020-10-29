from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.views.generic.base import View
import requests

from .oauth_client import OAuthClient


class GithubOAuthMixin:
    client_id = None
    secret = None
    callback_url = None
    scopes = None

    def get_client_id(self):
        return self.client_id or settings.GITHUB_OAUTH_CLIENT_ID

    def get_secret(self):
        return self.secret or settings.GITHUB_OAUTH_SECRET

    def get_callback_url(self):
        url = self.callback_url or settings.GITHUB_OAUTH_CALLBACK_URL
        return self.request.build_absolute_uri(url)

    def get_scopes(self):
        return self.scopes or getattr(settings, 'GITHUB_OAUTH_SCOPES', [])

    def get_client(self):
        kwargs = {
            'client_id': self.get_client_id(),
            'secret': self.get_secret(),
            'callback_url': self.get_callback_url(),
            'scopes': self.get_scopes()
        }
        return OAuthClient(self.request, **kwargs)


class GithubOAuthLoginView(GithubOAuthMixin, View):

    def get(self, request, *args, **kwargs):
        client = self.get_client()
        return redirect(client.get_redirect_url())


class GithubOAuthCallbackView(GithubOAuthMixin, View):
    backend = None

    def get_backend(self):
        if self.backend:
            return backend
        if hasattr(settings, 'GITHUB_OAUTH_BACKEND'):
            return settings.GITHUB_OAUTH_BACKEND

    def get_user_model(self):
        return get_user_model()

    def get_login_redirect_url(self):
        return settings.LOGIN_REDIRECT_URL if settings.LOGIN_REDIRECT_URL else '/'

    def get_access_token(self):
        client = self.get_client()
        return client.get_access_token(self.request.GET['code'])

    def get(self, request, *args, **kwargs):
        token = self.get_access_token()
        headers = {'Authorization': 'token %s' % token}
        r = requests.get('https://api.github.com/user', headers=headers)
        data = r.json()
        defaults = dict(login=data['login'], token=token)
        user_model = self.get_user_model()
        user, _ = user_model.objects.update_or_create(defaults, id=data['id'])
        backend = self.get_backend()
        kwargs = {'backend': backend} if backend else {}
        login(request, user, **kwargs)
        if 'next' in request.GET:
            return redirect(request.GET['next'])
        return redirect(self.get_login_redirect_url())
