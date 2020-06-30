import setuptools

setuptools.setup(
    name='django-github-oauth',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
