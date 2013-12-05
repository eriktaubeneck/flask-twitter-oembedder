import requests
from requests_oauthlib import OAuth1
from flask import Markup

class TwitterOEmbedder(object):

    def __init__(self, app=None, cache=None, debug=None):
        if app and cache:
            self.init(app, cache, debug)

    def init(self, app, cache, timeout=None, debug=None):
        def _cache_key(func, *args, **kwargs):
            return (args[0], kwargs.get('omit_script', False))

        twitter_timeout = 60*60*24*365
        max_timeout = {'saslmemcached':60*60*24*30,
                       'simple': twitter_timeout}

        if not timeout:
            default_timeout = app.config.get('CACHE_DEFAULT_TIMEOUT', 300)
            timeout = min(max_timeout.get(app.config('CACHE_TYPE', default_timeout)),
                          twitter_timeout)

        @app.context_processor
        def tweet_processor():
            @cache.memoize(timeout=timeout)
            def oembed_tweet(tweet_id,
                             access_token=app.config['TWITTER_ACCESS_TOKEN'],
                             token_secret=app.config['TWITTER_TOKEN_SECRET'],
                             omit_script=False):
                auth = OAuth1(app.config['TWITTER_CONSUMER_KEY'],
                              app.config['TWITTER_CONSUMER_SECRET'],
                              access_token,
                              token_secret)
                url = 'https://api.twitter.com/1.1/statuses/oembed.json'
                params = {'id':tweet_id,
                          'omit_script':omit_script}
                r = requests.get(url, params=params, auth=auth)
                try:
                    tweet_html = Markup(r.json()[u'html'])
                except KeyError as e:
                    if debug or (debug is None and app.debug):
                        raise e
                    else:
                        return ''
                return tweet_html
            oembed_tweet.make_cache_key = _cache_key
            return dict(oembed_tweet=oembed_tweet)
