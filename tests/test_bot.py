import httpretty
import pytest
from twitterbot.TwitterBot import TwitterBot


@pytest.fixture
def bot():
    consumer_key = "consumer_key"
    consumer_secret = "consumer_secret"
    key = "key"
    secret = "secret"
    return TwitterBot(consumer_key, consumer_secret, key, secret)


@pytest.fixture
def tweet():
    return {
        "created_at": "Fri Aug 02 03:11:44 +0000 2019",
        "id": 1157126808590082048,
        "id_str": "1157126808590082048",
        "text": "RT @rebeccaballhaus: Jason Statham negotiated a deal limiting how badly he can be beaten up. Vin Diesel has his sister police the # of punc\u2026",
        "truncated": False,
        "entities": {
            "hashtags": [],
            "symbols": [],
            "user_mentions": [
                {
                    "screen_name": "rebeccaballhaus",
                    "name": "Rebecca Ballhaus",
                    "id": 705706292,
                    "id_str": "705706292",
                    "indices": [3, 19],
                }
            ],
            "urls": [],
        },
        "source": '<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>',
        "in_reply_to_status_id": None,
        "in_reply_to_status_id_str": None,
        "in_reply_to_user_id": None,
        "in_reply_to_user_id_str": None,
        "in_reply_to_screen_name": None,
        "user": {
            "id": 3359131192,
            "id_str": "3359131192",
            "name": "salah ahmed",
            "screen_name": "salah_halas_",
            "location": "New York, NY",
            "description": "",
            "url": "https://t.co/ltjzIWZQHs",
            "entities": {
                "url": {
                    "urls": [
                        {
                            "url": "https://t.co/ltjzIWZQHs",
                            "expanded_url": "http://salahahmed.me",
                            "display_url": "salahahmed.me",
                            "indices": [0, 23],
                        }
                    ]
                },
                "description": {"urls": []},
            },
            "protected": False,
            "followers_count": 70,
            "friends_count": 393,
            "listed_count": 1,
            "created_at": "Sat Jul 04 18:12:02 +0000 2015",
            "favourites_count": 2505,
            "utc_offset": None,
            "time_zone": None,
            "geo_enabled": False,
            "verified": False,
            "statuses_count": 599,
            "lang": None,
            "contributors_enabled": False,
            "is_translator": False,
            "is_translation_enabled": False,
            "profile_background_color": "000000",
            "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
            "profile_background_tile": False,
            "profile_image_url": "http://pbs.twimg.com/profile_images/1139836444778754049/JDSKPYll_normal.jpg",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/1139836444778754049/JDSKPYll_normal.jpg",
            "profile_banner_url": "https://pbs.twimg.com/profile_banners/3359131192/1437970233",
            "profile_link_color": "19CF86",
            "profile_sidebar_border_color": "000000",
            "profile_sidebar_fill_color": "000000",
            "profile_text_color": "000000",
            "profile_use_background_image": False,
            "has_extended_profile": False,
            "default_profile": False,
            "default_profile_image": False,
            "following": False,
            "follow_request_sent": False,
            "notifications": False,
            "translator_type": "none",
        },
        "geo": None,
        "coordinates": None,
        "place": None,
        "contributors": None,
        "retweeted_status": {
            "created_at": "Thu Aug 01 17:48:27 +0000 2019",
            "id": 1156985053597097984,
            "id_str": "1156985053597097984",
            "text": "Jason Statham negotiated a deal limiting how badly he can be beaten up. Vin Diesel has his sister police the # of p\u2026 https://t.co/v5shOiuzVZ",
            "truncated": True,
            "entities": {
                "hashtags": [],
                "symbols": [],
                "user_mentions": [],
                "urls": [
                    {
                        "url": "https://t.co/v5shOiuzVZ",
                        "expanded_url": "https://twitter.com/i/web/status/1156985053597097984",
                        "display_url": "twitter.com/i/web/status/1\u2026",
                        "indices": [117, 140],
                    }
                ],
            },
            "source": '<a href="https://about.twitter.com/products/tweetdeck" rel="nofollow">TweetDeck</a>',
            "in_reply_to_status_id": None,
            "in_reply_to_status_id_str": None,
            "in_reply_to_user_id": None,
            "in_reply_to_user_id_str": None,
            "in_reply_to_screen_name": None,
            "user": {
                "id": 705706292,
                "id_str": "705706292",
                "name": "Rebecca Ballhaus",
                "screen_name": "rebeccaballhaus",
                "location": "Washington, D.C.",
                "description": "White House reporter at @WSJ",
                "url": "https://t.co/BzzVgFj1vG",
                "entities": {
                    "url": {
                        "urls": [
                            {
                                "url": "https://t.co/BzzVgFj1vG",
                                "expanded_url": "https://www.wsj.com/news/author/7537",
                                "display_url": "wsj.com/news/author/75\u2026",
                                "indices": [0, 23],
                            }
                        ]
                    },
                    "description": {"urls": []},
                },
                "protected": False,
                "followers_count": 71471,
                "friends_count": 1846,
                "listed_count": 1711,
                "created_at": "Thu Jul 19 20:12:07 +0000 2012",
                "favourites_count": 2886,
                "utc_offset": None,
                "time_zone": None,
                "geo_enabled": True,
                "verified": True,
                "statuses_count": 18255,
                "lang": None,
                "contributors_enabled": False,
                "is_translator": False,
                "is_translation_enabled": False,
                "profile_background_color": "FF6699",
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme19/bg.gif",
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme19/bg.gif",
                "profile_background_tile": False,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1011677272561025029/pFFA3nTS_normal.jpg",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1011677272561025029/pFFA3nTS_normal.jpg",
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/705706292/1546664300",
                "profile_link_color": "B40B43",
                "profile_sidebar_border_color": "FFFFFF",
                "profile_sidebar_fill_color": "F6FFD1",
                "profile_text_color": "333333",
                "profile_use_background_image": True,
                "has_extended_profile": False,
                "default_profile": False,
                "default_profile_image": False,
                "following": False,
                "follow_request_sent": False,
                "notifications": False,
                "translator_type": "none",
            },
            "geo": None,
            "coordinates": None,
            "place": None,
            "contributors": None,
            "is_quote_status": False,
            "retweet_count": 2893,
            "favorite_count": 8111,
            "favorited": True,
            "retweeted": True,
            "possibly_sensitive": False,
            "lang": "en",
        },
        "is_quote_status": False,
        "retweet_count": 2893,
        "favorite_count": 0,
        "favorited": True,
        "retweeted": True,
        "lang": "en",
    }


@httpretty.activate
def test_get(bot, tweet):
    httpretty.register_uri(
        httpretty.GET, bot.my_tweets_url, json=[tweet], status=200
    )
    response, tweets = bot.get_my_tweets()
    assert response.status == 200


@httpretty.activate
def test_delete(bot, tweet):
    tweet_id = 1
    httpretty.register_uri(
        httpretty.POST, bot.delete_url(tweet_id), json=tweet, status=200
    )
    response, tweet = bot.delete_tweet(tweet_id)
    assert response.status == 200
