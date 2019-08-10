import datetime as dt
import json

from argparse import ArgumentParser
from .utils import get_bot


def main():
    args = get_args()
    twitterbot = get_bot()
    response, my_tweets = twitterbot.get_my_tweets(args.max_id)
    datetime_format = "%a %b %d %H:%M:%S +0000 %Y"
    x_days_ago_from_now = dt.datetime.utcnow() - dt.timedelta(days=args.days)
    for tweet in my_tweets:
        tweet_time = dt.datetime.strptime(tweet["created_at"], datetime_format)
        if tweet_time < x_days_ago_from_now:
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
