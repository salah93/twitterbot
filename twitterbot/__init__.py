import json
import os
import oauth2 as oauth

from argparse import ArgumentParser
try:
    # Python 2.6-2.7
    from urllib import urlencode
except ImportError:
    # Python 3
    from urllib.parse import urlencode


class TwitterBot():
    def __init__(
            self,
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret):
        self.client = self.__signin(
                consumer_key,
                consumer_secret,
                access_token,
                access_token_secret)
        self.search_url = 'https://api.twitter.com/1.1/search/tweets.json?'

    def __signin(self, consumer_key, consumer_secret, key, secret):
        consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
        token = oauth.Token(key=key, secret=secret)
        return oauth.Client(consumer, token)

    def search(self,
               query,
               geocode=None,
               lang=None,
               locale=None,
               result_type=None,
               count=None,
               until=None,
               since_id=None,
               max_id=None,
               include_entities=None):
        q = dict(
            q=query,
            geocode=geocode,
            lang=lang,
            locale=locale,
            result_type=result_type,
            count=count,
            until=until,
            since_id=since_id,
            max_id=max_id,
            include_entities=include_entities)
        search_query = {}
        for k, v in q.items():
            if v is not None:
                search_query[k] = v
        url = self.search_url + urlencode(search_query)
        resp, content = self.client.request(
            url.encode('ascii'),
            method='GET',
            body=''.encode('utf-8'),
            headers=None)
        return resp, json.loads(content.decode('utf-8'))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('query')
    args = parser.parse_args()
    consumer_key = os.environ['TWITTER_CONSUMER_KEY']
    consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
    key = os.environ['TWITTER_ACCESS_TOKEN']
    secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    twitter = TwitterBot(consumer_key, consumer_secret, key, secret)
    content = twitter.search(args.query)
    print(content)
