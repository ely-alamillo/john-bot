import tweepy
from time import sleep
from credentials import *

# set up auth with tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

js_tweets = tweepy.Cursor(api.search, q = '#React', lang='en').items(10)

for tweet in js_tweets:
    try:
        print('tweeted by: @%s' % tweet.user.screen_name)

        # retweet the tweet
        tweet.retweet()
        print('retweeted the tweet')

        # favorite tweet
        tweet.favorite();
        print('favorited the tweet')

        # followed user
        if not tweet.user.following:
            tweet.user.follow()
            print('followed the user')
        sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        print('stopping the bot')
        break
