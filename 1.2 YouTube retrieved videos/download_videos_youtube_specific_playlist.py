# -*- coding: utf-8 -*-
"""
This code downloads videos from a given youtube playlist url 

INPUT
    - A youtube playlist url
OUTPUT
    - A csv file with the video ids that belong to the given playlist
    - A directory with the downloaded videos

NOTES:
    - Be careful to be on path: 
        D:\itzel\PhD Computer Science\github-codes\dcc-hsdvmi-video-dataset\1.2 YouTube retrieved videos
    - It is recommendable that the playlist url corresponds to the url from the first video on the list 
    (in order to also retrieve the channel name)
    
@author: itzel
last edited: 23-08-27
"""

from pytube import YouTube
from pytube import Playlist
import re
import os
import csv
import time

def save_videoids_from_yt_playlist(playlist_url, lst_videos):
    output_path = "1.2.1 YT videos (lists of IDs)/" 
    csv_file_name = "yt-videos-from-playlist-" + playlist_url.split("=")[-1] + ".csv"
    
    myFile = open(output_path + csv_file_name, 'w', newline='')
    writer = csv.writer(myFile)
    writer.writerow(['Video ID', 'Video URL', 'Playlist URL'])
    for video_data in lst_videos:
        writer.writerow(video_data)
    myFile.close()
    
def download_from_Youtube(video_id, video_url, output_dir_path):
    yt = YouTube(video_url, use_oauth=False, allow_oauth_cache=True) # create a YouTube object with the video URL
    #video = yt.streams.first()
    video = yt.streams.get_highest_resolution() # get the highest quality video stream
    #print(output_dir_path + "/" + video_id)
    video.download(output_dir_path + "/", video_id+".mp4")
    
def download_videos_from_yt_playlist(playlist_url, output_dir_path):
    if not os.path.exists(output_dir_path):
        os.mkdir(output_dir_path)
    totalSuccessfullAttempts=0
    missingVideos=0
    lst_video_ids = []
    playlist = Playlist(playlist_url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    i = 1
    print("# Videos: ", len(playlist.video_urls))
    for video_url in playlist.video_urls:
        video_id = video_url.split('v=')[1]
        lst_video_ids.append([video_id, video_url, playlist_url])
        # Downloading the video
        try:
            download_from_Youtube(video_id, video_url, output_dir_path)
            totalSuccessfullAttempts += 1   
            print(str(i) + " Video ID: " + video_id + "\t"+ "Video DOWNLOADED ")     
        except:
            missingVideos +=1
            print(str(i) + " Video ID: " + video_id + "\t"+ "Unable to download video ") 
        i = i + 1
    save_videoids_from_yt_playlist(playlist_url, lst_video_ids)                 
                
if __name__ == "__main__":
    playlist_url = input("YouTube playlist URL: ")    
    channel_name = playlist_url.split('=')[-1]
    output_dir= "1.2.2 YT videos (downloaded)/dwnld-yt-playlist-" + channel_name
    
    download_videos_from_yt_playlist(playlist_url, output_dir)
