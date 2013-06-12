"""
Flask-Twitter-OEmbedder
-----------------------

Embedded tweets in Flask Jinja2 Templates with only the Tweet_ID
"""
from setuptools import setup

setup(
    name = "Flask-Twitter-OEmbedder",
    version = '0.1.0',
    url = 'https://github.com/eriktaubeneck/flask-twitter-oembedder',
    license = 'MIT',
    author = 'Erik Taubeneck',
    author_email = 'erik.taubeneck@gmail.com',
    description = 'Embedded tweets in Flask Jinja2 Templates with only the Tweet_ID',
    py_modules = ['flask_twitter_oembedder'],
    include_package_data = True,
    platforms = 'any',
    install_requires = [
        'Flask',
        'requests',
        'requests-oauthlib',
        'Flask-Cache'
        ]
)