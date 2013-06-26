"""
Flask-Twitter-OEmbedder
-----------------------

Embedded tweets in Flask Jinja2 Templates with only the Tweet_ID
"""
from setuptools import setup

setup(
    name = "Flask-Twitter-OEmbedder",
    version = '0.1.2',
    url = 'https://github.com/eriktaubeneck/flask-twitter-oembedder',
    license = 'MIT',
    author = 'Erik Taubeneck',
    author_email = 'erik.taubeneck@gmail.com',
    description = 'Embedded tweets in Flask Jinja2 Templates with only the Tweet_ID',
    py_modules = ['flask_twitter_oembedder'],
    zip_safe=False,
    platforms = 'any',
    include_package_data=True,
    test_suite="tests",
    install_requires=[
        'Flask',
        'Flask-Cache',
        'requests',
        'requests_oauthlib',
        ],
    tests_require=[
        'Flask-Testing',
        'Flask-Cache',
        'httpretty',
        ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)
