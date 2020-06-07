from setuptools import setup

setup(
    name='django-github-oauth',
    version='2020.6.3',
    install_requires=[
        'Django',
        'django-passwordless-auth',
        'django-passwordless-user',
        'requests',
        'setuptools',
    ],
    packages=[
        'django_github_oauth',
        'django_github_oauth.migrations',
    ],
)
