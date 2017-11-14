# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Variables that contains the user credentials to access Twitter API
consumer_key = "LSnYD9PVZaL7B6CfKUMBRJNjr"
consumer_secret = "PfX8XvkxffnyTIRHYb5CsWn7JrbqoJaW7qq64RQnCsOPkNlr6k"
access_token = "929862495745007617-CCPgOz9Mdv1fIQc5YMqJg5XF9xD3tMw"
access_token_secret = "1GKGWFPdVnfZWMWZg6m4Fg1foCeys4nkWqNKe1OStNgpG"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(json.loads(data)["text"])
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['python', 'javascript', 'ruby'])
