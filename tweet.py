# General:
import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing
import re

# For plotting and visualization:
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
#matplotlib inline

# Twitter App access keys for @user

# Consume:
CONSUMER_KEY    = '4glklFBMR5blxsr63Ywe7OrYR'
CONSUMER_SECRET = 's5c2zuAOmHS84k78yFIyyDMuyCXJx4Jgjv6qwSRT8VR4cAQl6G'

# Access:
ACCESS_TOKEN  = '1305461708-fXs7MLmqOHmHtTU77F1I6I318HuLtsvpFaXbeLq'
ACCESS_SECRET = 'vpJSD6cj4A173L2rj6peto1ph52npMGbNnRPxU5RNnQI0'

# We import our access keys:
#from credentials import *    # This will allow us to use the keys as variables

# API's setup:
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

    # We create an extractor object:
api = twitter_setup()

# We create a tweet list as follows:
#tweets = extractor.user_timeline(screen_name="EmmaWatson", count=200)
#print("Number of tweets extracted: {}.\n".format(len(tweets)))

# We print the most recent 5 tweets:
#print("5 recent tweets:\n")
#for tweet in tweets[:5]:
    #print(tweet.text)
    #print()

tweets = tweepy.Cursor(api.search, q='hattrick').items(100)


#Creating a (pandas) DataFrame
# We create a pandas dataframe as follows:
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

# We display the first 10 elements of the dataframe:
display(data.tail(5))

#Extracting hashtags


#def extract_hash_tags(s):
#return set([re.sub(r"(\W+)$", "", j) for j in set([i for i in text.split() if i.startswith("#")])])
