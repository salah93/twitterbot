import os
from ..TwitterBot import TwitterBot


def get_bot():
    consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
    consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
    key = os.environ["TWITTER_ACCESS_TOKEN"]
    secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
    return TwitterBot(consumer_key, consumer_secret, key, secret)
