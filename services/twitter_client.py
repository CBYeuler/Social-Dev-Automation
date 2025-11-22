import tweepy
import os

def get_twitter_client():
    auth = tweepy.OAuth1UserHandler(
        os.getenv("TWITTER_API_KEY"),
        os.getenv("TWITTER_API_SECRET"),
        os.getenv("TWITTER_ACCESS_TOKEN"),
        os.getenv("TWITTER_ACCESS_SECRET")
    )
    return tweepy.API(auth)

def post_tweet(text: str):
    client = get_twitter_client()
    client.update_status(text)


