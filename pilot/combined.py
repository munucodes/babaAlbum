import os
import glob
from pydub import AudioSegment
from pathlib import Path
from pytube import Playlist

#downloader part

# Set the directory where the downloaded files will be saved
dir_path = 'D:\\birSarkidirYasamak\\Kocekceler'

# Create a Playlist object from a YouTube playlist URL
playlist = Playlist("https://www.youtube.com/watch?v=6az5k9y-Hs0&list=OLAK5uy_lNWIJASOhSHI8UrfYymLs_LH_JtAXRzXw")

print('Number of videos in playlist: %s' % len(playlist.video_urls))

# Loop through all videos in the playlist and download them
for v, video in enumerate(playlist.videos, start=1):
    # Download the first audio-only stream
    stream = video.streams.filter(only_audio=True).first().download(dir_path)
    
    print(stream.title)    
    print(video.title)
    
    # Check if a file with the video title already exists in the directory
    old_file_path = Path(os.path.join(dir_path, f"{video.title}.mp4"))
    if old_file_path.is_file():
        # If such a file exists, rename the file by prepending the counter v and a hyphen to the video title
        new_file_path = os.path.join(dir_path, f"{v}-{video.title}.mp4")
        os.rename(old_file_path, new_file_path)


#converter part
# Path where the videos are located
video_dir = Path('D:\\birSarkidirYasamak\\Kocekceler')  
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

