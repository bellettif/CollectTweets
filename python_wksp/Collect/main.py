'''
Created on Oct 27, 2014

@author: cusgadmin
'''

from slistener import SListener
import time, tweepy, sys

## authentication
consumer_key = '2jIENdsU3BmmVXUyZdl9tB1G4'
consumer_secret = 'dz47PmsbhhG1AntbdPUxnZFnAjJPNr5bQTovNUKF67QrFpgIDF'
access_token = '1958979090-fmatN9JqCeEVKgW8bLAymS1O3IMegxpBrNmFv9L'
access_token_secret = 'b7DPeZGjOOlZLc9khHP3wMMMFJmFVdUaZcLnqlFogFXMI'

api = tweepy.API(auth)

def main():
    track = ['obama', 'romney']
 
    listen = SListener(api, 'myprefix')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try: 
        stream.filter(track = track)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()