from distutils.core import setup

setup(
    name='bomberman-python',
    version='0.5.0',
    summary='Python client for interacting with Bomberman profanity filtering HTTP API.',
    home_page='http://bomberman.ikayzo.com',
    author='Ikayzo',
    author_email='bomberman-support@ikayzo.com',
    packages=['bomberman',],
    license='MIT',
    long_description=open('README.md').read(),
)
