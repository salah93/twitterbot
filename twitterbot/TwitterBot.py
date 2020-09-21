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

    def __signin(self):
        consumer = oauth.Consumer(
            key=self.__consumer_key, secret=self.__consumer_secret
        )
        token = oauth.Token(key=self.__key, secret=self.__secret)
        return oauth.Client(consumer, token)

    @property
    def trending_url(self):
        return "https://api.twitter.com/1.1/trends/place.json?"

    @property
    def tweets_url(self):
        return "https://api.twitter.com/1.1/statuses/user_timeline.json?"

    def delete_url(self, tweet_id):
        return "https://api.twitter.com/1.1/statuses/destroy/{id}.json?".format(
            id=tweet_id
        )

    @property
    def my_favorites_url(self):
        return "https://api.twitter.com/1.1/favorites/list.json?"

    @property
    def remove_favorite_url(self):
        return "https://api.twitter.com/1.1/favorites/destroy.json?"

    def get_trending(self, where_on_earth_id=1):
        search_query = {"id": where_on_earth_id}
        url = self.trending_url + urlencode(search_query)
        response, tweets = self.__client.request(
            url.encode("ascii"), method="GET", body="".encode("utf-8"), headers=None
        )
        return response, json.loads(tweets.decode("utf-8"))

    def get_my_tweets(self, max_id=None, count=200):
        return self.get_tweets(max_id=max_id, count=count)

    def delete_tweet(self, tweet_id):
        url = self.delete_url(tweet_id)
        response, tweet = self.__client.request(
            url, method="POST", body="".encode("utf-8"), headers=None
        )
        return response, json.loads(tweet.decode("utf-8"))

    def get_my_favorites(self, max_id=None, count=200):
        search_query = {"count": count}
        if max_id is not None:
            search_query["max_id"] = max_id
        url = self.my_favorites_url + urlencode(search_query)
        response, tweets = self.__client.request(
            url.encode("ascii"), method="GET", body="".encode("utf-8"), headers=None
        )
        return response, json.loads(tweets.decode("utf-8"))

    def remove_favorite(self, tweet_id):
        search_query = {"id": tweet_id}
        url = self.remove_favorite_url + urlencode(search_query)
        response, tweet = self.__client.request(
            url, method="POST", body="".encode("utf-8"), headers=None
        )
        return response, json.loads(tweet.decode("utf-8"))

    def get_tweets(self, screen_name=None, max_id=None, count=5):
        search_query = {"count": count}
        if screen_name is not None:
            search_query["screen_name"] = screen_name
        if max_id is not None:
            search_query["max_id"] = max_id
        url = self.tweets_url + urlencode(search_query)
        response, tweets = self.__client.request(
            url.encode("ascii"), method="GET", body="".encode("utf-8"), headers=None
        )
        return response, json.loads(tweets.decode("utf-8"))
