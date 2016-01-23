'''
Created on Oct 27, 2014

@author: cusgadmin
'''

import tweepy
import ConfigParser
import os, sys
import cPickle as pickle

OUTPUT_DIR = 'dump'

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        timestamp = status.created_at.strftime('%Y-%m-%d_%H')
        if timestamp not in os.listdir(OUTPUT_DIR):
            os.mkdir(('%s/%s') % (OUTPUT_DIR, timestamp))
        pickle.dump(status, open('%s/%s/tweet_%s.pi' % (OUTPUT_DIR, timestamp, status.id_str), 'wb'))
        print 'Pickling ' + str(status.created_at)
        
 
consumer_key = '2jIENdsU3BmmVXUyZdl9tB1G4'
consumer_secret = 'dz47PmsbhhG1AntbdPUxnZFnAjJPNr5bQTovNUKF67QrFpgIDF'
access_token = '1958979090-fmatN9JqCeEVKgW8bLAymS1O3IMegxpBrNmFv9L'
access_token_secret = 'b7DPeZGjOOlZLc9khHP3wMMMFJmFVdUaZcLnqlFogFXMI' 

if OUTPUT_DIR not in os.listdir('./'):
    os.mkdir(OUTPUT_DIR)

while True:
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        streaming_api = tweepy.streaming.Stream(auth, Listener(), timeout=10)
        # New York area
        streaming_api.filter(locations=[-74.05,
                                        40.66,
                                        -73.90,
                                        40.85])
    except Exception as e:
        print e