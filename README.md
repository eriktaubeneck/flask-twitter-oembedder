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

The `twitter_access_token` and `twitter_token_secret` can also be passed into the `oembed_tweet` function as they may change if you have multiple users authenticating into your site.

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

Flask-Twitter-OEmbedder users the `@app.context_processor` decorator to expose the `oembed_tweet()` function inside of the Jinja2 templates. In order to use this for some `tweet_id`, just include the following in your template

    {{ oembed_tweet(tweet_id) }}

and the corresponding html for that tweet will be embedded in the page.  You should also see the [Embedded Tweets](https://dev.twitter.com/docs/embedded-tweets) documentation from Twitter.

By default, twitter will include the following inclusion of `widget.js` in the embedded tweet. However, if you want to track intensions, you can omit this reference by calling the `oembed_tweet` fuction the following way:

    {{ oembed_tweet(tweet_id, omit_script=True) }}

If you do this, you will need to include the following JavaScript somewhere in the page:

    <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>


Debuging
--------

By default, Flask-Twitter-OEmbedder will return an empty string for any input into the function which Twitter does not return an appropriate response to. This is ideal in production, as you likely don't want your entire application to crash because a Tweet ID doesn't work (this could happen not only in error, for example the tweeter could have deleted their tweet or the twitter API could be down for the moment). However, when debugging it may be desirable to actually raise the error and bring you to the build in Flask debugger (assuming you have set `app.debug = True` as well). By default, Flask-Twitter-OEmbedder will inherit the `app.debug` state, however you can override this with the following:

    twitter_oembedder = TwitterOEmbedder(app,cache,debug=True)

or

    twitter_oembedder = TwitterOEmbedder(app,cache,debug=False)

or

    twitter_oembedder = TwitterOEmbedder()
    ...
    twitter_oembedder.init(app,cache,debug=True)

or

    twitter_oembedder = TwitterOEmbedder()
    ...
    twitter_oembedder.init(app,cache,debug=False)

It should also be noted that when changing the debug state, you should clear your cache, otherwise existing calls will returned the cached result.
