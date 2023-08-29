# -*- coding: utf-8 -*-
# pip install --upgrade google-api-python-client
"""
This code receives a list of words.
Each one is used as a query to filter youtube video ids related to that word.

INPUT
    - A csv file that contains a list of words
    - n_retrieved_videos as the number of videos to retrieve for each word in the list
OUTPUT
    - A csv file that contains information of the retrieved video (Query, Video ID, Video URL, Title)

NOTES:
    - Be careful to be on path: 
        \dcc-hsdvmi-video-dataset\1.2 YouTube retrieved videos
    - api key source: 
        https://console.cloud.google.com/apis/credentials?project=dcc-hsdvmi-yt&supportedpurview=project
    
@author: itzel
last edited: 23-08-22
"""

import csv
from googleapiclient.discovery import build
import pandas as pd
import time
import os

# Set up the API key and build the YouTube service
api_key = "" 
youtube = build('youtube', 'v3', developerKey=api_key)

def search_videos(query, n):
    # Adding symbol '-' previous to a word excludes the word from the query search
    total_query = query + ' -"letra" -"lyrics" -"Letra" -"Lyrics"'
    # Calling the API to search for videos based on the query
    # NOTE: Daily quota is 10,000 and search request is 100 units
    search_response = youtube.search().list(
        part='snippet',
        q=total_query,
        type='video',
        maxResults=n,
        relevanceLanguage="es",  
        regionCode="MX",
        videoDuration="medium",
    ).execute()
    # videoDuration with medium parameter considers videos between 4 and 20 min long 
    # YT API https://developers.google.com/youtube/v3/docs/search/list
    
    retrieved_videos = []
    # Extracting video information from the API response
    for item in search_response['items']:
        word = query
        video_id = item['id']['videoId']
        video_url =  "https://www.youtube.com/watch?v=" + item['id']['videoId']
        video_title = item['snippet']['title']        
        channel_id = item['snippet']['channelId']
        channel_name = item['snippet']['channelTitle']

        retrieved_videos.append((word, video_id, video_url, video_title, channel_id, channel_name))
        # Time sleep is necessary because the YT API establish a limited number of queries in certain time  
        time.sleep(2)  
    return retrieved_videos

def scrape_youtube_videos(input_csv_file, output_csv_file_name, n):
    df = pd.read_csv(input_csv_file)  
    lst_words = df['words'] # from the list of hate speech words
    
    lst_all_videos = []
    w=0
    for word in lst_words:
        w = w + 1
        print(w, "Word:", word)
        lst_all_videos = lst_all_videos + search_videos(word, n)
    
    # Write the video data to a new CSV file
    with open(output_csv_file_name, "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(['Query', 'Video ID', 'Video URL', 'Video Title', 'Channel ID', 'Channel Name'])
        writer.writerows(lst_all_videos)

if __name__ == "__main__":
    #path_general = "/dcc-hsdvmi-video-dataset/"
    
    path_words_lists = "../1.1 hate speech words lists/"
    # INPUT CSV FILES
    input_csv = path_words_lists + "lst-hs-word-seeds-sre-56w.csv"
    #input_csv = path_words_lists + "lst-hs-word-seeds-hatebase-29w.csv"
    
    n_retrieved_videos = 15
    
    path_output_result = "1.2.1 YT videos (lists of IDs)/"
    # OUTPUT CSV FILES
    output_csv = path_output_result + "yt-filtered-videos-from-lst-sre-n" + str(n_retrieved_videos) + "-vpw.csv"
    #output_csv = path_output_result + "yt-filtered-videos-from-lst-hatebase-n" + str(n_retrieved_videos) + "-vpw.csv"
     
    #dfsample = write_sample(input_csv, output_csv)
    
    scrape_youtube_videos(input_csv, output_csv, n_retrieved_videos)
 
