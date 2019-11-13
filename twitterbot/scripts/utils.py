from ..TwitterBot import TwitterBot
from operator import itemgetter

import datetime as dt
import itertools
import logging
import os
import random
import time


def get_bot():
    logger = logging.getLogger(__name__)
    try:
        consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
        consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
        key = os.environ["TWITTER_ACCESS_TOKEN"]
        secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
    except KeyError:
        logger.exception('bad config')
        raise RuntimeError
    return TwitterBot(consumer_key, consumer_secret, key, secret)


def get_oldest_tweet(get_tweets_fn, days, max_id=None):
    logger = logging.getLogger(__name__)
    x_days_ago_from_now = dt.datetime.utcnow() - dt.timedelta(days=days)
    datetime_format = "%a %b %d %H:%M:%S +0000 %Y"

    def is_tweet_younger_than_x_days(tweet):
        tweet_time = dt.datetime.strptime(tweet["created_at"], datetime_format)
        return tweet_time >= x_days_ago_from_now

    def loop(max_id=None):
        response, my_tweets = get_tweets_fn(max_id=max_id)
        try:
            if response.status == 429:
                raise RuntimeError("rate limit exceeded")
            elif response.status == 401:
                raise RuntimeError("bad authentication")
        except RuntimeError:
            logger.exception("could not get tweets")
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


def configure_logger(level=logging.INFO):
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    handler.setLevel(level)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level)
