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

for tweet in tweepy.Cursor(api.user_timeline, id="realDonaldTrump").items(100):
    incorrect = False
    try:
        new_tweet = str(tweet.text).split()
    except:
        continue
    for word in new_tweet:
        if not word:
            #checks if the word is empty
            break
        elif word == "RT":
            #ignore word
            # short for retweet
            break
        elif word == "&amp;":
            #ignore word
            #for some reason, tweepy interprets the '&' to '&amp;'
            break
        elif word.startswith("#"):
            break
            #ignore word because this is a "trend"
        elif word.startswith("@"):
            #ignore word because this is a username
            break
        elif word.startswith("http"):
            # this is a link...ignore as well
            break
        elif word == "Obama":
            # enchant sees this as not a word
            break
        elif word == "Facebook":
            # enchant sees this as not a word
            break
        elif word == "Healthcare":
            # enchant sees this as not a word
            break
        elif ("'" in word) and not str(word).startswith("'") and not str(word).endswith("'") :
            # if there is an apostrophe in between a word, it usually means it was a conjuntion
            # if there is an apostrophe at the end or the begininng, it usually means that it is part of a quote
            break
        elif "..." in word:
            if "...." in word:
                word = str.replace(word, "....", " ")
            else:
                word = str.replace(word, "...", " ")
            new_word = str(word).split()
            for temp in new_word:
                temp = temp.strip()
                if not dict.check(temp):
                    print ("WRONG: %s" % temp)
                    incorrect = True
            break
        elif "/" in word:
            word = str.replace(word, "/", " ")
            new_word =str(word).split()
            for temp in new_word:
                temp = temp.strip()
                if not dict.check(temp):
                    print ("WRONG: %s" % temp)
                    incorrect = True
            break
        else:
            #this line removes all special charaters
            word = re.sub('\W+','', word)
            if not word:
                # if the "word" was only a special character, then it breaks out of the second loop
                break
            if not dict.check(word):
                print ("WRONG: %s" % word)
                incorrect = True

    if incorrect == True:
        print "INCORRECT TWEET: %s" % tweet.text

'''import enchant

dict = enchant.Dict("en_US")

file = open("trump.txt", "w")

file.close'''
