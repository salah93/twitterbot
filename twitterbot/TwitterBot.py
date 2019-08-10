from urllib.parse import urlencode

import json
import oauth2 as oauth


class TwitterBot:
    def __init__(
        self, consumer_key, consumer_secret, access_token, access_token_secret
    ):
        self.__consumer_key = consumer_key
        self.__consumer_secret = consumer_secret
        self.__key = access_token
        self.__secret = access_token_secret
        self.__client = self.__signin()

    def delete_url(self, tweet_id):
        return "https://api.twitter.com/1.1/statuses/destroy/{id}.json?".format(
            id=tweet_id
        )

    @property
    def my_tweets_url(self):
        return "https://api.twitter.com/1.1/statuses/user_timeline.json?"

    def __signin(self):
        consumer = oauth.Consumer(
            key=self.__consumer_key, secret=self.__consumer_secret
        )
        token = oauth.Token(key=self.__key, secret=self.__secret)
        return oauth.Client(consumer, token)

    @property
    def trending_url(self):
        return "https://api.twitter.com/1.1/trends/place.json?"

    def get_my_tweets(self, max_id=None):
        search_query = {"count": 200}
        if max_id:
            search_query["max_id"] = max_id
        url = self.my_tweets_url + urlencode(search_query)
        response, tweets = self.__client.request(
            url.encode("ascii"), method="GET", body="".encode("utf-8"), headers=None
        )
        return response, json.loads(tweets.decode("utf-8"))

    def get_trending(self, where_on_earth_id=1):
        search_query = {"id": where_on_earth_id}
        url = self.trending_url + urlencode(search_query)
        response, tweets = self.__client.request(
            url.encode("ascii"), method="GET", body="".encode("utf-8"), headers=None
        )
        return response, json.loads(tweets.decode("utf-8"))

    def delete_tweet(self, tweet_id):
        url = self.delete_url(tweet_id)
        response, tweet = self.__client.request(
            url, method="POST", body="".encode("utf-8"), headers=None
        )
        return response, json.loads(tweet.decode("utf-8"))
