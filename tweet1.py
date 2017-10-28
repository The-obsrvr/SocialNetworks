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
#Extracting hashtags
def extract_hash_tags(text):
	return set([re.sub(r"(\W+)$", "", j) for j in set([i for i in text.split() if i.startswith("#")])])
def extract_mentions(text):
	return set([re.sub(r"(\W+)$", "", j) for j in set([i for i in text.split() if i.startswith("@")])])
# We print the most recent 5 tweets:
#print("5 recent tweets:\n")
#for tweet in tweets[:5]:
    #print(tweet.text)
    #print()
tweets = tweepy.Cursor(api.search, q='#iphone', include_entities=True, lang="en").items(200)
a=[(tweet.text,tweet.created_at,tweet.retweet_count,tweet.user.screen_name) for tweet in tweets]                 

#for i in tweets:
	#print (i.text)

#Creating a (pandas) DataFrame
# We create a pandas dataframe as follows:
twetexts = [x[0] for x in a]
twedate = [x[1] for x in a]
tweret = [x[2] for x in a]
tweuse = [x[3] for x in a]
data = pd.DataFrame(data=twetexts, columns=['Tweets'])
#Storing 
data['HashTags'] = np.array([(extract_hash_tags(i)) for i in data['Tweets']])
data['Mentions'] = np.array([(extract_mentions(i)) for i in data['Tweets']])
data['Date'] = np.array(twedate)
data['RTs']    = np.array(tweret)
data['User'] = np.array(tweuse)
data.sort_values(by='Date', ascending=0)
htlist = list(list(data['HashTags'][a]) for a in range(0,len(data)))
#implementing as a dictionary in a dictionary
from collections import defaultdict
com = defaultdict(lambda : defaultdict(int))
for k in range(0,len(htlist)):    
    for i in range(len(htlist[k])-1):            
        for j in range(i+1, len(htlist[k])):
            w1, w2 = sorted([htlist[k][i], htlist[k][j]])                
            if w1 != w2:
                com[w1][w2] += 1
com_max = []
# For our term, look for the most common co-occurrent terms
for t1 in com:
    if(t1 == '#iphone'):
        t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
        for t2, t2_count in t1_max_terms:
            com_max.append(((t1, t2), t2_count))
# Get the most frequent co-occurrences
terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
print(terms_max[:5])

    
