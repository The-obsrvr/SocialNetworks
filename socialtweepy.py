from tweepy.streaming import Stream
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
# for all the tutorials and code refer https://pythonprogramming.net/twitter-api-streaming-tweets-python-tutorial/?completed=/mysql-live-database-example-streaming-data/
ckey="Ht2hjyNon1BgyMxhBhbC2reSF"
csecret="1REwJr4uTdTVKVlMTmbeNBPDDEJJuQspdZD7kpc0f7U4AkQHI4"
atoken="738527443-xXzYkJ8SEIZuCI4dCAoPLmV6rwi8joLDR226BirC"
asecret="fD8JdWcNaO3TFiUQMQm5yrFkHWGDEJpXBmpnAYccS4lpM"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])

#only for reference
