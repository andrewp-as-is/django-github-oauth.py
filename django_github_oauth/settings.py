import os

GITHUB_OAUTH_CLIENT_ID    = os.getenv('DJANGO_GITHUB_OAUTH_CLIENT_ID')
GITHUB_OAUTH_SECRET       = os.getenv('DJANGO_GITHUB_OAUTH_SECRET')
GITHUB_OAUTH_CALLBACK_URL = os.getenv('DJANGO_GITHUB_OAUTH_CALLBACK_URL')
GITHUB_OAUTH_SCOPES       = os.getenv('DJANGO_GITHUB_OAUTH_SCOPES').split(',')

# optional - User model, fields: login, token
# INSTALLED_APPS+=['django_github_oauth']
# AUTH_USER_MODEL = 'django_github_oauth.User'
# AUTHENTICATION_BACKENDS = ('django_passwordless_auth.backend.PasswordlessAuthBackend',)
