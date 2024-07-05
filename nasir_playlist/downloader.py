# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:51:19 2024

@author: z004ax9h
"""
import pytube
from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

playlist = Playlist("https://www.youtube.com/watch?v=2wA77jcvxYE&list=PL9yMuNaTmLB7Pt9P592eU9RuIXh1leYZo")

#prints each video url, which is the same as iterating through playlist.video_urls
for url in playlist:
    print(url)
#prints address of each YouTube object in the playlist
for vid in playlist.videos:
    print(vid)
    
