from ..TwitterBot import TwitterBot
from operator import itemgetter

import datetime as dt
import itertools
import logging
import os
import random
import time


def get_bot():
    consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
    consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
    key = os.environ["TWITTER_ACCESS_TOKEN"]
    secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
    return TwitterBot(consumer_key, consumer_secret, key, secret)


def get_oldest_tweet(get_tweets_fn, days, max_id=None):
    logger = get_logger(__name__)

    x_days_ago_from_now = dt.datetime.utcnow() - dt.timedelta(days=days)
    datetime_format = "%a %b %d %H:%M:%S +0000 %Y"

    def is_tweet_younger_than_x_days(tweet):
        tweet_time = dt.datetime.strptime(tweet["created_at"], datetime_format)
        return tweet_time >= x_days_ago_from_now

    def loop(max_id=None):
        for i in range(2):
            response, my_tweets = get_tweets_fn(max_id=max_id)
            if response.status == 429:
                logger.debug("rate limit exceeded")
                secs = random.choice(range(2, 6))
                logger.debug("sleeping %s seconds" % secs)
                time.sleep(secs)
            if response.status == 200:
                break
        else:
            raise RuntimeError("rate limit exceeded")
        logger.info("my tweets %s" % [t["id"] for t in my_tweets])
        old_tweets = list(itertools.dropwhile(is_tweet_younger_than_x_days, my_tweets))
        if len(old_tweets):
            first_old_tweet_id = old_tweets[0]["id"]
            logger.debug("found oldest %s" % first_old_tweet_id)
            return first_old_tweet_id
        elif len(my_tweets) <= 1:
            logger.debug("couldnt find anything %s" % my_tweets)
            raise RuntimeError
        else:
            max_id = my_tweets[-1]["id"]
            logger.debug("still looking for oldest %s" % max_id)
            return loop(max_id)

    logger.debug("looking for oldest")
    return loop(max_id)


def get_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    ch = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
