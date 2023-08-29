# -*- coding: utf-8 -*-
# !pip install pytube==10.4.1
# !pip install -U get-video-properties

"""
This code receives a list of youtube video IDs and download the videos into a directory

INPUT
    - A csv file that contains a list of Video IDs (from YouTube) 
OUTPUT
    - A folder with the downloaded videos
    
@author: itzel
last edited: 23-08-22
"""

from pytube import YouTube
import os
import pandas as pd
import time

def download_from_Youtube(filename, dir_name, video_url):
    yt = YouTube(video_url, use_oauth=False, allow_oauth_cache=True) # create a YouTube object with the video URL
    #video = yt.streams.first()
    video = yt.streams.get_highest_resolution() # get the highest quality video stream
    
    dwnld_video = video.download(dir_name + "/")
    extension = dwnld_video.split(".")[-1]
    youtube_id_filename = filename + "." + extension
    os.rename(dwnld_video, dir_name + "/" + youtube_id_filename)    
        
def download_videos_set(input_csv_file, output_dir_path):
    csvFile = pd.read_csv(input_csv_file)
    filename = input_csv_file.split('/')[-1].split('.')[0]
    # Directory where the videos are gonna be saved
    dir_name = output_dir_path + "dwnld-" + filename
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    
    totalSuccessfullAttempts=0
    missingVideos=0
    for i, video_URL in enumerate(csvFile["Video URL"]):
        if(i==0 or (csvFile["Video URL"][i-1] not in video_URL)):
            try:
                if "youtube" in video_URL:
                    download_from_Youtube(csvFile["Video ID"][i], dir_name, video_URL)
                    print(i, "Video ID: " +"\t"+csvFile["Video ID"][i] +"\t URL: \t"+ video_URL+"\t"+ "Video DOWNLOADED ")
                    totalSuccessfullAttempts+=1
                    time.sleep(5)
            except:
                print(i, "Video ID: " +"\t"+csvFile["Video ID"][i] +"\t URL: \t"+ video_URL+"\t"+ "Unable to download video ")
                missingVideos+=1
    print("Total Successfull Attempts = ", totalSuccessfullAttempts)
    print("Missing Videos = ", missingVideos)
    

if __name__ == "__main__":
    path_to_yt_video_lsts = "1.2.1 YT videos (lists of IDs)/"
    # INPUT CSV FILES
    input_csv = path_to_yt_video_lsts + "yt-filtered-videos-from-lst-sre-n3-vpw.csv" 
    #input_csv = path_to_yt_video_lsts + "yt-filtered-videos-from-lst-hatebase-n3-vpw.csv"
    
    # OUTPUT DIR
    output_dir = "1.2.2 YT videos (downloaded)/"
    
    download_videos_set(input_csv, output_dir)
    
