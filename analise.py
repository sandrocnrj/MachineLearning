import numpy as np
import pandas as pd
import tweepy
import matplotlib as plt
import seaborn as sns
import textblob
from IPython.display import display
from credencial import *
from textblob import TextBlob 
import re

import MySQLdb as mdb
import sys

try:
    con = mdb.connect('localhost', 'usuario', 'senha', 'database');
    cur = con.cursor()
    cur.execute('SELECT VERSION()')
    ver = cur.fetchone()    
    print 'Database version : %s'  % ver
    
except mdb.Error, e:  
    print 'Error %d:' %s % (e.args[0],e.args[1])
    sys.exit(1)


def twitter_setup():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
 
    api = tweepy.API(auth)
    return api

extractor = twitter_setup()

tweets = extractor.user_timeline(screen_name="usuario", count=200)
print("Quantidade de tweets retornados: {}.\n".format(len(tweets)))

i = 0 
for tweet in tweets:
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO tabela (coluna1) VALUES(%s)" % (tweets[i].favorite_count))
        i = i + 1


#data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
#display(data.head(10))

#print(tweets[0].id)
#print(tweets[0].created_at)
#print(tweets[0].source)
#print(tweets[0].favorite_count)
#print(tweets[0].retweet_count)
#print(tweets[0].geo)
#print(tweets[0].coordinates)
#print(tweets[0].entities)

#data['len'] = np.array([len(tweet.text) for tweet in tweets])
#data['ID'] = np.array([tweet.id for tweet in tweets])
#data['Date'] = np.array([tweet.created_at for tweet in tweets])
#data['Source'] = np.array([tweet.source for tweet in tweets])
#data['Likes'] = np.array([tweet.favorite_count for tweet in tweets])
#data['RTs'] = np.array([tweet.retweet_count for tweet in tweets])

#mean = np.mean(data['len'])
 
#print("A media do tamanho dos tweets: {}".format(mean))

#fav_max = np.max(data['Likes'])
#rt_max = np.max(data['RTs'])
 
#fav = data[data.Likes == fav_max].index[0]
#rt = data[data.RTs == rt_max].index[0]
 
#print("O tweet com mais likes: {}".format(data['Tweets'][fav].encode('utf-8')))
#print("Numero de likes: {}".format(fav_max))
#print("{} caracteres.".format(data['len'][fav]))
 
#print("o tweet com o mais retweets: {}".format(data['Tweets'][rt].encode('utf-8')))
#print("Numero de retweets: {}".format(rt_max))
#print("{} caracteres.".format(data['len'][rt]))

#tlen = pd.Series(data=data['len'].values, index=data['Date'])
#tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
#tret = pd.Series(data=data['RTs'].values, index=data['Date'])
 
# grafico do tamanho dos tweets ao longo do tempo.
#tlen.plot(figsize=(16,4), color='r');
