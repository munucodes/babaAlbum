# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 12:29:35 2024

@author: z004ax9h
"""

import os
import glob
from pydub import AudioSegment

video_dir = 'D:\\birSarkidirYasamak\\IstanbulTurkuleri2'  # Path where the videos are located
extension_list = ('*.mp4', '*.flv', '*.webm')


os.chdir(video_dir)
for extension in extension_list:
    for video in glob.glob(extension):
        mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
        print('converting : ' + mp3_filename)
        AudioSegment.from_file(video).export(mp3_filename, format='mp3')