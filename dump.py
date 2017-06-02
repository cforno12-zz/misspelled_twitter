import tweepy
from tweepy import OAuthHandler

c_key = 'oMqmiuz8Q3Ff5oOWtXRCPgQzc'
c_secret = '5pLT9xTIY02FnPXthnPDC0aOIwlYF9gWcjoUyP8ca2W6ofCiZO'
a_token = '527005919-jN34yfTmGA7oq4DyQOfmoOMldz5mGSyulNYovFtH'
a_secret = 'wipjyYEbRxVrINKq2HxJukWDnC8fXUzx4sC80taAbd32I'

auth = OAuthHandler(c_key, c_secret)
auth.set_access_token(a_token, a_secret)

api = tweepy.API(auth)

import enchant
import re

dict = enchant.Dict("en_US")

for tweet in tweepy.Cursor(api.user_timeline, id="realDonaldTrump").items(50):
    incorrect = False
    try:
        new_tweet = str(tweet.text).split()
    except:
        continue
    for word in new_tweet:
        if not word:
            break
        elif word == "RT":
            #ignore word
            break
        elif word == "&amp;":
            #ignore word
            break
        elif word.startswith("#"):
            break
            #ignore word
        elif word.startswith("@"):
            #ignore word
            break
        elif word.startswith("http"):
            # this is a link...ignore as well
            break

        word = re.sub('\W+','', word)
        if not word:
            break
        if dict.check(word):
            # spelling is correct
            pass
        else:
            print("WRONG: %s" % word)
            incorrect = True

    if incorrect == True:
        print "INCORRECT TWEET: %s" % tweet.text

'''import enchant

dict = enchant.Dict("en_US")

file = open("trump.txt", "w")

file.close'''
