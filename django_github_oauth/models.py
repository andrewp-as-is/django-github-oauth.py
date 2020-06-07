from django.db import models
from django_passwordless_user.models import AbstractBaseUser

class User(AbstractBaseUser):
    login = models.TextField(unique=True)
    token = models.TextField()

    USERNAME_FIELD = 'login'

    class Meta:
        db_table = 'github_oauth_user'

    def get_avatar_url(self):
        return 'https://github.com/%s.png' % (self.login,)

    def get_salted_hmac_value(self):
        return self.token
