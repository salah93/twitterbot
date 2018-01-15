import pytest
from os import environ

from twitterbot import TwitterBot


@pytest.fixture
def bot():
    consumer_key = environ['TWITTER_CONSUMER_KEY']
    consumer_secret = environ['TWITTER_CONSUMER_SECRET']
    key = environ['TWITTER_ACCESS_TOKEN']
    secret = environ['TWITTER_ACCESS_TOKEN_SECRET']
    for k in [consumer_secret, consumer_key, key, secret]:
        assert k
    bot = TwitterBot(consumer_key, consumer_secret, key, secret)
    return bot


def test_search(bot):
    query = 'bored'
    resp, content = bot.search(query)
    assert resp.status == 200
