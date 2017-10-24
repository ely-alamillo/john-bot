import tweepy
from time import sleep
from credentials import *

# set up auth with tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# open the book
mysteries = open('mysteriesOfAllNation.txt', 'r')

# read lines from the book
mystery_lines = mysteries.readlines();

# close the file read stream
mysteries.close()

for line in mystery_lines:
    # catch errors for duplicate tweets
    try:
        # no errors will tweet
        # print(line)
        # if line is not blank tweet
        if line != '\n':
            print('tweeting some line')
            api.update_status(line)
        # if line is blank don't tweet
        else:
            print('blank line yo')
            pass
    # handles the error
    except tweepy.TweepError as e:
        print(e.reason)
    print('going to sleep')
    sleep(5)
