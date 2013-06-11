import requests
from flask import Markup

class FlaskTwitterOEmbedder(object):
    
    def __init__(self, app=None, cache=None):
        if app is not None and cache is not None:
            self.init(app, cache)
    
    def init(self, app, cache):
        @cache.memoize(timeout=60*60*24*356)
        @app.context_processor
        def twitter_oembed(tweet_id):
            url = 'https://api.twitter.com/1/statuses/oembed.json'
            payload = {'id':tweet_id}
            r = requests.get(url, params=payload)
            return Markup(r.json()['html'])
