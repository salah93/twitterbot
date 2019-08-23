import json
import logging

from argparse import ArgumentParser
from .utils import get_bot, get_oldest_tweet, configure_logger


def main():
    configure_logger()
    logger = logging.getLogger(__name__)
    args = get_args()
    twitterbot = get_bot()
    try:
        first_old_tweet_id = get_oldest_tweet(
            twitterbot.get_my_tweets, args.days, args.max_id
        )
    except RuntimeError:
        old_tweets = []
    else:
        _, old_tweets = twitterbot.get_my_tweets(max_id=first_old_tweet_id)
    logger.info('found %s tweets' % len(old_tweets))
    for tweet in old_tweets:
        response, deleted_tweet = twitterbot.delete_tweet(tweet["id"])
        print(json.dumps(deleted_tweet))


def get_args():
    parser = ArgumentParser()
    parser.add_argument("days", type=int, help="tweets older than this will be deleted")
    parser.add_argument("--max_id")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
