from ast import If
from fileinput import filename
from pytube import YouTube
from pytube import Playlist
import re
# from tqdm import tqdm
import os

import time
import sys


def compet():

    print(name + "\nDownloading Complete")


def progress_function(chunk, file_handle, bytes_remaining):
    filesizee = video[0].filesize
    current = ((filesizee - bytes_remaining)/filesizee)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write('{name} ↳ |{bar}| {percent}%\r'.format(name=name, bar=status, percent=percent))
    # sys.stdout.flush()


link = input('Enter the Link \n')
playlist = Playlist(link)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
video_count = playlist.video_urls
tut_name = input('Enter the Tutorial Name \n')

num = 1
for i, url in enumerate(video_count):
    yt = YouTube(url)
    video = yt.streams.filter(
        progressive=True, file_extension='mp4', resolution='720p')
    name = str(num) + " " + tut_name + ".mp4"
    check_name = f"D:/Coding/Programming Video/{tut_name}/" + name
    if os.path.exists(check_name):
        print(name + "already exsists")
        num = num+1
        continue
    else:
        print("Title : ", yt.title)
        size = str(video[0].filesize/(1024*1024))
        print("\nFilesize : " + size + "MB")
        yt.register_on_progress_callback(progress_function)
        out_file = video[0].download(f'D:/Coding/Programming Video/{tut_name}', filename=name)
        video[0].on_complete(compet())
        num = num+1
