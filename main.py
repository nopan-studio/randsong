#!/usr/bin/env python
from ytmusicapi import YTMusic
import random
import time
import os 
import sys 
random.seed(time.time())
ytmusic = YTMusic()

#swappable variables
browser = "chromium"

def viewResults(search):
    search = ytmusic.search(search,"songs",30)
    for s in search:
        artist = s.get("artists")
        artist = artist[0]
        if str(s.get("videoId")) != "None":
            print("Artist: "+artist.get("name"))
            print("Title: "+s.get("title"))
            print("Video ID : "+str(s.get("videoId"))) 
            print(" ")

def randomMusic(search):
    search = ytmusic.search(search,"songs",30)
    random.seed(time.time()*100.001)
    rand = random.randint(1,len(search))
    iterator = 1
    for s in search:
        if iterator == rand:
            if str(s.get("videoId")) != "None" :
                print("Title: "+s.get("title"))
                print("Video ID : "+str(s.get("videoId")))
                os.system("notify-send \"Song Name : " + s.get("title")+"\"")
                os.system(browser+" music.youtube.com/watch?v="+s.get("videoId")+" &")
            else:
                rand += 1
        iterator += 1

# main shit. 
if len(sys.argv) > 1:
    #viewResults(str(sys.argv[1]))
    randomMusic(str(sys.argv[1]))
    #viewResults("mamamoo")
else:
    print("usage : main.py \"artist_name\" ")

