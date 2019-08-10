import json
import yweather

from argparse import ArgumentParser
from .utils import get_bot


def main():
    args = get_args()
    twitterbot = get_bot()
    client = yweather.Client()
    where_on_earth_id = client.fetch_woeid(args.location_name) if args.location_name else 1
    if where_on_earth_id is None:
        raise ValueError("could not find 'where on earth id' of the location given")
    response, trending_tweets = twitterbot.get_trending(where_on_earth_id)
    print(json.dumps(trending_tweets))


def get_args():
    parser = ArgumentParser()
    parser.add_argument(
        "-l",
        "--location_name",
        help="city or country name, leave blank for global",
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
