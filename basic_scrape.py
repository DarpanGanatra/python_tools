import tweepy
from textblob import TextBlob

consumer_key= 'KOt4R4JAATFdgOMfDIptdii4W'
consumer_secret = 'OpacoRnzqhIUXNdAWAFNSraCgWL7Te1bSjuTMFZcY8BZr0l046'

access_token='348130213-RX4GViYmJtkK45zFb1EDUAVk9z1WG86J2wVLabFa'
access_token_secret='BpfircrE0ZryooeYNMpyiuCoU4OSeu3rpBLJiBQ6v83uE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
