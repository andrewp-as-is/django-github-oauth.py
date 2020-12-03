import setuptools

setuptools.setup(
    name='django-github-oauth',
    version='2020.11.1',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
