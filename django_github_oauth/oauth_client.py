from django.conf import settings
from django.utils.http import urlencode
import requests

class OAuthClient(object):
    def __init__(self, request):
        self.request = request
        self.callback_url = request.build_absolute_uri(settings.GITHUB_OAUTH_CALLBACK_URL)

    def get_redirect_url(self):
        scopes = getattr(settings,'GITHUB_OAUTH_SCOPES',[])
        return 'https://github.com/login/oauth/authorize?%s' % urlencode({
            'client_id': settings.GITHUB_OAUTH_CLIENT_ID,
            'redirect_uri': self.callback_url,
            'scope': ' '.join(set(scopes if scopes else [])),
            'response_type': 'code'
        })

    def get_access_token(self, code):
        data = {
            'code': code,
            'client_id': settings.GITHUB_OAUTH_CLIENT_ID,
            'client_secret': settings.GITHUB_OAUTH_SECRET,
            'grant_type': 'authorization_code',
            'redirect_uri': self.callback_url
        }
        r = requests.post('https://github.com/login/oauth/access_token',data=data)
        r.raise_for_status()
        for s in filter(lambda s:'access_token' in s,r.text.split('&')):
            return s.split('=')[1]

