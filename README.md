[![](https://img.shields.io/badge/released-2020.11.1-green.svg?longCache=True)](https://pypi.org/project/django-github-oauth/)
[![](https://img.shields.io/badge/license-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)

### Installation
```bash
$ pip install django-github-oauth
```

### How it works
1.   [create OAuth app](https://github.com/settings/developers)
2.    edit settings `GITHUB_OAUTH_CLIENT_ID` and `GITHUB_OAUTH_SECRET`
3.    add login and callback urls

#### `settings.py`
```python
GITHUB_OAUTH_CLIENT_ID = os.getenv('DJANGO_GITHUB_OAUTH_CLIENT_ID')
GITHUB_OAUTH_SECRET = os.getenv('DJANGO_GITHUB_OAUTH_SECRET')
GITHUB_OAUTH_CALLBACK_URL = os.getenv('DJANGO_GITHUB_OAUTH_CALLBACK_URL')
GITHUB_OAUTH_SCOPES = []

AUTH_USER_MODEL = 'users.User'
AUTHENTICATION_BACKENDS = ('django_github_oauth.backend.Backend',) # passwordless auth
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```
#### `urls.py`
```python
urlpatterns+= [
    path('login', include('django_github_oauth.urls.login')),
    path('login-github-callback', include('django_github_oauth.urls.callback')),
    path('logout', include('django_github_oauth.urls.logout')),
]
```
