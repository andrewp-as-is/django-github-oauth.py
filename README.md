<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-github-oauth.svg?maxAge=3600)](https://pypi.org/project/django-github-oauth/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-github-oauth.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-github-oauth.py/actions)

### Installation
```bash
$ [sudo] pip install django-github-oauth
```

##### `settings.py`
```python
INSTALLED_APPS+=['django_github_oauth']

GITHUB_OAUTH_CLIENT_ID = os.getenv('DJANGO_GITHUB_OAUTH_CLIENT_ID')
GITHUB_OAUTH_SECRET = os.getenv('DJANGO_GITHUB_OAUTH_SECRET')
GITHUB_OAUTH_CALLBACK_URL = os.getenv('DJANGO_GITHUB_OAUTH_CALLBACK_URL')
GITHUB_OAUTH_SCOPES = []

# optional - User model, fields: login, token
AUTH_USER_MODEL = 'django_github_oauth.User'
AUTHENTICATION_BACKENDS = ('django_passwordless_auth.backend.PasswordlessAuthBackend',)
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

[django-github-oauth-configuration (django-configurations)](https://pypi.org/project/django-github-oauth-configuration/)

##### `urls.py`
```python
urlpatterns+= [
    path('github-oauth/', include('django_github_oauth.urls')),
]
```

```html
{% url 'github_oauth:login' %}
{% url 'github_oauth:callback' %}
{% url 'github_oauth:logout' %}
```

custom urls:
```python
from django_github_oauth_views.views import GithubOAuthLoginView
from views import CallbackView

urlpatterns = [
    path('login', GithubOAuthLoginView.as_view()),
    path('callback', GithubOAuthCallbackView.as_view())
]
```

##### `views.py`
custom callback
```python
from django_github_oauth.views import GithubOAuthCallbackView
from django_github_oauth.models import User

class GithubOAuthCallbackView(GithubOAuthCallbackView):
    def get(self,request, *args, **kwargs):
        headers = {'Authorization': 'token %s' % self.token}
        r = requests.get('https://api.github.com/user', headers=headers)
        data = r.json()
        defaults = dict(login=data['login'],token=self.token)
        user,created = User.objects.update_or_create(defaults,id=data['id'])
        ...
```

#### Links
+   [django-github-oauth-configuration (django-configurations)](https://pypi.org/project/django-github-oauth-configuration/)
+   [github.com/settings/developers](https://github.com/settings/developers)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>