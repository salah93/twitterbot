[![Build Status](https://travis-ci.org/salah93/twitterbot.svg?branch=master)](https://travis-ci.org/salah93/twitterbot)

# Twitter Bot
twitter bot
+ delete tweets
+ get trending tweets

## Install
` pip install salahs-twitterbot `

## Twitter API
- create a new [twitter application](https://apps.twitter.com/)
- save consumer key, consumer secret, access  key and access secret as environment variables

```
export TWITTER_CONSUMER_KEY='aaaaaaaaaaaaaaaaaaaaaaaaa'
export TWITTER_CONSUMER_SECRET='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
export TWITTER_ACCESS_TOKEN='aaaaaaaaaa-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
export TWITTER_ACCESS_TOKEN_SECRET='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
```

- `delete_old_tweets --help`
- `get_trending_tweets --help`
