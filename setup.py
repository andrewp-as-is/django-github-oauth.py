import setuptools

setuptools.setup(
    name='django-github-oauth',
    version='2020.10.29',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
