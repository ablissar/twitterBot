# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json
# from pprint import pprint

# Variables that contains the user credentials to access Twitter API
consumer_key = "LSnYD9PVZaL7B6CfKUMBRJNjr"
consumer_secret = "PfX8XvkxffnyTIRHYb5CsWn7JrbqoJaW7qq64RQnCsOPkNlr6k"
access_token = "929862495745007617-CCPgOz9Mdv1fIQc5YMqJg5XF9xD3tMw"
access_token_secret = "1GKGWFPdVnfZWMWZg6m4Fg1foCeys4nkWqNKe1OStNgpG"

stream = None
api = None


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        data = json.loads(data)
        print(data['text'] + "\n")
        tweet_id = data['id']
        api.create_favorite(tweet_id)
        return True

    def on_error(self, status):
        print(status)


def init():
    global stream, api
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    l = StdOutListener()
    stream = Stream(auth, l)
    api = tweepy.API(auth)


if __name__ == '__main__':
    init()
    stream.filter(follow=['2414818604', '930260779332505600'])
