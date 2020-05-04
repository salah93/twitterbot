# Twitter Bot
twitter bot
+ delete tweets
+ get trending tweets

## Install
` pip install salahs-twitterbot[scripts]`

## Twitter API
- create a new [twitter application](https://apps.twitter.com/)
- save consumer key, consumer secret, access  key and access secret as environment variables

```
cat <<EOF > keys.env
export TWITTER_CONSUMER_KEY='aaaaaaaaaaaaaaaaaaaaaaaaa'
export TWITTER_CONSUMER_SECRET='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
export TWITTER_ACCESS_TOKEN='aaaaaaaaaa-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
export TWITTER_ACCESS_TOKEN_SECRET='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
EOF
source keys.env
```

- `delete_old_tweets --help`
- `get_trending_tweets --help`
- `remove_favorites --help`
