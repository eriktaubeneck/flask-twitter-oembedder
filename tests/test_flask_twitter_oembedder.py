from flask import Flask, render_template_string, Markup
from flask.ext.testing import TestCase, ContextVariableDoesNotExist
from flask.ext.cache import Cache
from flask.ext.twitter_oembedder import TwitterOEmbedder
import types
import httpretty


class FlaskStaticTest(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING']=True
        app.config['CACHE_TYPE'] = 'simple'
        app.config['TWITTER_CONSUMER_KEY'] = 'twitter_consumer_key'
        app.config['TWITTER_CONSUMER_SECRET'] = 'twitter_consumer_secret'
        app.config['TWITTER_ACCESS_TOKEN'] = 'twitter_access_token'
        app.config['TWITTER_TOKEN_SECRET'] = 'twitter_token_secret'
        self.cache = Cache(app)      
        self.twitter_oembedder = TwitterOEmbedder(app,self.cache)

        @app.route('/')
        def index():
            return render_template_string('')
        
        return app


    def test_jinja_oembed_tweet_avaliable(self):
        response = self.client.get('/')
        assert type(self.get_context_variable('oembed_tweet')) is types.FunctionType

    @httpretty.activate    
    def test_oembed_tweet_valid_id_debug_off(self):
        with open('tests/data/99530515043983360.json') as f:
            httpretty.register_uri(httpretty.GET, 'https://api.twitter.com/1.1/statuses/oembed.json?id=99530515043983360',
                body = f.read())
        response = self.client.get('/')
        oembed_tweet = self.get_context_variable('oembed_tweet')
        valid = oembed_tweet('99530515043983360')
        assert type(valid) is Markup
    
    @httpretty.activate
    def test_oembed_tweet_invaild_id_debug_off(self):
        with open('tests/data/abc.json') as f:
            httpretty.register_uri(httpretty.GET, 'https://api.twitter.com/1.1/statuses/oembed.json?id=abc',
                body = f.read())
        response = self.client.get('/')
        oembed_tweet = self.get_context_variable('oembed_tweet')
        invalid = oembed_tweet('abc')
        assert invalid is ''
    
    @httpretty.activate    
    def test_oembed_tweet_invalid_id_debug_on(self):
        self.twitter_oembedder.init(self.app, self.cache, debug=True)
        with open('tests/data/abc.json') as f:
            httpretty.register_uri(httpretty.GET, 'https://api.twitter.com/1.1/statuses/oembed.json?id=abc',
                body = f.read())
        response = self.client.get('/')
        oembed_tweet = self.get_context_variable('oembed_tweet')
        try:
            invalid = oembed_tweet('abc')
            assert False
        except Exception as e:
            assert type(e) is KeyError
    






