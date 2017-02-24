#!/usr/bin/env python
from twython import Twython, TwythonError
import time

# Insert your keys here.
APP_KEY = 'XXXXXXXXXXXXX'
APP_SECRET = 'XXXXXXXXXXXXX'
OAUTH_TOKEN = 'XXXXXXXXXXXXX'
OAUTH_TOKEN_SECRET = 'XXXXXXXXXXXXX'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
    with open('facts.txt', 'r+') as tweetfile:
        buff = tweetfile.readlines()

    for line in buff[:]:
        line = line.strip(r'\n')  # Strips any empty line.
        if len(line) <= 140 and len(line) > 0:
            print ("Tweeting...")
            twitter.update_status(status=line)
            with open('liners.txt', 'w') as tweetfile:
                buff.remove(line)  # Removes the tweeted line.
                tweetfile.writelines(buff)
            time.sleep(900)
        else:
            # Removes the line that has more than 140 characters.
            with open('liners.txt', 'w') as tweetfile:
                buff.remove(line)
                tweetfile.writelines(buff)
            print ("Skipped line - Char length violation")
            continue

    # When you see this... Go find some new tweets...
    print ("No more lines to tweet...")


except TwythonError as e:  # Prints errors if any occur.
    print (e)
