Flask Twitter OEmbedder
=======================

Purpose
-------

The Twitter API V1.1 provides an endpoint for easily [embedding tweets](https://dev.twitter.com/docs/api/1.1/get/statuses/oembed) into your webpages. However, Twitter rate limits this endpoint and requires authorization. Flask Twitter OEmbedder gets your Twitter credentials from your `app.config` and exposes the `oembed_tweet` function to the Jinja templates. Flask Twitter OEmbedder also manages the caching of the tweets, given an arbitrary cache using Flask-Cache.

Install
-------

To install `flask-twitter-oembedder`, use [pip](http://pip.readthedocs.org/en/latest/).

    $ pip install flask-twitter-oembedder

You can also install from source by cloning this Git repository and running `python setup.py install`.

Usage
-----

Since the Twitter API V1 has been officially shut down, the V1.1 requires OAuth authentication. If you do not have a developer account with Twitter, go [here](https://dev.twitter.com/) to sign up for free.  Include your keys and secrets in your `app.config` like so:

    app.config['TWITTER_CONSUMER_KEY'] = 'consumer_key
    app.config['TWITTER_CONSUMER_SECRET'] = 'consumer_secret'
    app.config['TWITTER_ACCESS_TOKEN'] = 'access_token'
    app.config['TWITTER_TOKEN_SECRET'] = 'token_secret'

Twitter also requires you to cache the html that you receive from this endpoint. Flask-Twitter-OEmbedder is designed to work with [Flask-Cache](http://pythonhosted.org/Flask-Cache/). The `app` and `cache` object can either be submitted when the `Twitter_OEmbedder` object is created, as so

    from flask import Flask
    from flask.ext.twitter_oembedder import TwitterOEmbedder
    
    app = Flask(__name__)
    twitter_oembedder = TwitterOEmbedder(app,cache)

or later at configuration time using the `init` method:

    twitter_oembedder = TwitterOEmbedder()
    
    app = Flask(__name__)
    cache = Cache(app)
    
    twitter_oembedder.init(app,cache)

