from django.urls import path
from django.conf.urls import include

app_name = 'github_oauth'

urlpatterns = [
    path('callback', include('django_github_oauth.urls.callback')),
    path('login', include('django_github_oauth.urls.login')),
    path('logout', include('django_github_oauth.urls.logout')),
]
