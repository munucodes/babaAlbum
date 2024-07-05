# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:51:19 2024

@author: z004ax9h
"""
# import pytube
# from pytube import YouTube
# from pytube import Playlist
import os
# import moviepy.editor as mp
# import re

# playlist = Playlist("https://www.youtube.com/watch?v=2wA77jcvxYE&list=PL9yMuNaTmLB7Pt9P592eU9RuIXh1leYZo")

# #prints each video url, which is the same as iterating through playlist.video_urls
# for url in playlist:
#     print(url)

# for url in playlist:
#     YouTube(url).streams.first().download('D:\\babaAlbum\\birSarkidirYasamak')
from pathlib import Path
from pytube import Playlist



    
dir = 'D:\\birSarkidirYasamak\\Kocekceler'
playlist = Playlist("https://www.youtube.com/watch?v=6az5k9y-Hs0&list=OLAK5uy_lNWIJASOhSHI8UrfYymLs_LH_JtAXRzXw")

print('Number of videos in playlist: %s' % len(playlist.video_urls))
v = 1
# Loop through all videos in the playlist and download them
for video in playlist.videos:
    stream = video.streams.filter(only_audio=True).first().download(dir )
    print(stream.title)    
    print(video.title)
    no = str(v)
    my_file = Path(dir + '\\' + video.title + '.mp4')
    if my_file.is_file():
        os.rename(dir + '\\' + video.title + '.mp4', dir + '\\' + str(v) + '-' + video.title + '.mp4')
    v += 1