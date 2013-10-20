import requests
from requests_oauthlib import OAuth1
from flask import Markup

class TwitterOEmbedder(object):

    def __init__(self, app=None, cache=None, debug=None):
        if app and cache:
            self.init(app, cache, debug)
    def init(self, app, cache, debug=None):
        @app.context_processor
        def tweet_processor():
            @cache.memoize(timeout=60*60*24*356)
            def oembed_tweet(tweet_id,
                             omit_script=False,
                             access_token=app.config['TWITTER_ACCESS_TOKEN'],
                             token_secret=app.config['TWITTER_TOKEN_SECRET']):
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
            return dict(oembed_tweet=oembed_tweet)
