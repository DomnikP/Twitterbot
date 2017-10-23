import tweepy
from time import sleep

consumerKey        = #consumerKey des Accounts, mit dem man den Bot nutzen möchte
consumerSecret     = #consumerSecret des Accounts, mit dem man den Bot nutzen möchte
accessToken        = #accessToken des Accounts, mit dem man den Bot nutzen möchte
accessTokenSecret  = #accessTokenSecret des Accounts, mit dem man den Bot nutzen möchte

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='#sports', since='2017-10-01', until='2017-10-15',
                           geocode='37.3875,122.0575,5000km', lang='en').items(10000):
    try:
        # Username ausgeben
        print('\nTweet by: @' + tweet.user.screen_name)
        sleep(5)

        # Retweet
        tweet.retweet()
        print('Retweeted the tweet')

        # tweet liken
        tweet.favorite()
        print('Favorited the tweet')

        # User folgen
        if not tweet.user.following:
            tweet.user.follow()
            print('Followed the user')

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
