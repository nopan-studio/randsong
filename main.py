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
    search = ytmusic.search(search,"videos")
    for s in search:
        artist = s.get("artists")
        artist = artist[0]
        print("Artist: "+artist.get("name"))
        print("Title: "+s.get("title"))
        print("Video ID : "+s.get("videoId")) 
        #print(s)
        print(" ")

def randomMusic(search):
    search = ytmusic.search(search,"videos")
    random.seed(time.time()*100.001)
    rand = random.randint(1,len(search))
    iterator = 1
    for s in search:
        if iterator == rand:
            print("Title: "+s.get("title"))
            print("Video ID : "+s.get("videoId")) 
            os.system(browser+" music.youtube.com/watch?v="+s.get("videoId")+" &")
        iterator += 1

# main shit. 
if len(sys.argv) > 1:
    randomMusic(str(sys.argv[1]))
    #viewResults("mamamoo")
else:
    print("usage : main.py \"artist_name\" ")

