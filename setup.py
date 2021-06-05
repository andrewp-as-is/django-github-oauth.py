from setuptools import setup

setup(
    name='django-github-oauth',
    version='2020.11.1',
    install_requires=[
        'requests'
    ],
    packages=[
        'django_github_oauth',
        'django_github_oauth.migrations',
        'django_github_oauth.urls'
    ]
)
