import os
import glob
from pydub import AudioSegment
from pathlib import Path

# Path where the videos are located
video_dir = Path('D:\\birSarkidirYasamak\\IstanbulTurkuleri2')  
extension_list = ('*.mp4', '*.flv', '*.webm')

# Change the current working directory
os.chdir(video_dir)

# Loop through each extension type
for extension in extension_list:
    # Loop through each video with the current extension
    for video in glob.glob(extension):
        # Get the base name of the video and replace the extension with .mp3
        mp3_filename = video_dir / (os.path.splitext(video)[0] + '.mp3')
        print(f'converting : {mp3_filename}')
        
        # Convert the video to mp3 and export it
        AudioSegment.from_file(video).export(mp3_filename, format='mp3')