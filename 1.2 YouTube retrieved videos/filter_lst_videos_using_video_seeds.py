# -*- coding: utf-8 -*-
"""
This code retrieves YouTube videos related to a set of videos considered as seeds.

INPUT
    - A list of the Video IDs that will serve as the seeds
OUTPUT
    - A directory with the related videos and a csv file with the data of the related videos

NOTES:
    - Be careful to be on path: 
        \dcc-hsdvmi-video-dataset\1.2 YouTube retrieved videos
    - api key source: 
        https://console.cloud.google.com/apis/credentials?project=dcc-hsdvmi-yt&supportedpurview=project
    
@author: itzel
last edited: 23-08-25
"""

from googleapiclient.discovery import build
import pandas as pd
import os

# Set up the API key and build the YouTube service
api_key = "" 
youtube = build('youtube', 'v2', developerKey=api_key)

def get_related_videos(seed_video_id, n):
    # NOTE: Daily quota is 10,000 and search request is 100 units
    
    # IMPORTANT: The parameter relatedToVideoId has been DEPRECATED since August 7, 2023
    # https://developers.google.com/youtube/v3/revision_history#june-12,-2023
    
    search_response = youtube.search().list(
        type='video',
        relatedToVideoId=seed_video_id,
        part='snippet',
        maxResults=n,
        relevanceLanguage="es",  
    ).execute()
    # videoDuration with medium parameter considers videos between 4 and 20 min long 
    # YT API https://developers.google.com/youtube/v3/docs/search/list
    
    # Extract the related video details
    related_videos = []
    for item in search_response['items']:
        video_id = item['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"        
        video_title = item['snippet']['title']
        channel_id = item['snippet']['channelId']
        channel_name = item['snippet']['channelTitle']
        related_videos.append((video_id, video_url, video_title, channel_id, channel_name, seed_video_id))        
    return related_videos

def get_related_videos_from_lst_of_VIDEO_IDS(lst_all_related_videos, lst_ids_seed_videos, n):
    for video_id in lst_ids_seed_videos:
        print(video_id)
        # Call the function to get the related videos
        related_videos = get_related_videos(video_id, n)
        # Print the related video details
        for video in related_videos:
            print("Video ID:", video[0])
            print("Title:", video[1])
            print("--------------------")
        for v in related_videos:
            lst_all_related_videos.append(v) 
    return lst_all_related_videos
    
def get_lst_of_related_videos_from_a_video_seed(video_id, n):
    related_videos = get_related_videos(video_id, n)
    lst_related_videos = []
    for v in related_videos:
        lst_related_videos.append(v)
        #print(v)
    df_related_videos = pd.DataFrame(lst_related_videos,
                                     columns=['Video ID', 'Video URL', 'Video Title',
                                              'Channel ID', 'Channel Name', 'Seed Video ID'])
    return df_related_videos

def get_lst_files_from_directory(dir_path):
    lst_videos = os.listdir(dir_path)
    lst_ids_seed_videos = []
    for element in lst_videos:
        print(element)
        lst_ids_seed_videos.append(element.split('.')[0])
    return lst_ids_seed_videos
    


"""
Snippet of code to search related videos for an individual Video ID (seed)
INPUT: A video ID
OUTPUT: A data frame with the data of the n related videos
"""   
#df = get_lst_of_related_videos_from_a_video_seed("04jr6M_XS9I", n=5)

# ---------------------------------------------------------------------------- MAIN
"""
Snippet of code to search related videos for a list of Video IDs (video seeds)
INPUT: List of Video IDs
    - Option 1: You have a directory full of videos named by their ID. Then a list is generated from a given directory path.
    - Option 2: You have a csv file that specifies the Video IDs

OUTPUT: A data frame with the data of the n related videos
"""   
# For Option 1 uncomment/use this code
dir_dwnld_videos = "./1.2.2 YT videos (downloaded)/"
os.listdir(dir_dwnld_videos)

dir_name = "dwnld-yt-filtered-videos-from-lst-hatebase-n10-vpw-relevant" # edit the directory you wanna use
#dir_name = "dwnld-yt-filtered-videos-from-lst-sre-n10-vpw-relevant" # edit the directory you wanna use
dir_path = dir_dwnld_videos + dir_name
#os.listdir(dir_path)

lst_ids_seed_videos = get_lst_files_from_directory(dir_path)

# To eliminate video titles and only work with the available IDs
for i in lst_ids_seed_videos:
    if len(i) > 11:
        lst_ids_seed_videos.remove(i)
        print(i)


output_file_path = "./1.2.1 YT videos (lists of IDs)/"
output_file_name = '-'.join([str(item) for item in dir_name.split('-')[1:]])
print(output_file_name)

# SAVING THE SEED VIDEO IDs INTO A CSV 
dict = {'Video ID': lst_ids_seed_videos}
df = pd.DataFrame(dict)
df.to_csv(output_file_path + output_file_name + '.csv')

# -------------------------------------------------------------

# For Option 2 uncomment/use this code
#csv_file = output_file_path + "yt-filtered-videos-from-lst-hatebase-n10-vpw-relevant.csv"
csv_file = output_file_path + "yt-filtered-videos-from-lst-sre-n10-vpw-relevant.csv"
lst_ids_seed_videos = list(pd.read_csv(csv_file)['Video ID'])


# Retrieving related videos from video seeds
n = 5
lst_all_related_vids = []
lst_related_videos = get_related_videos_from_lst_of_VIDEO_IDS(lst_all_related_vids, lst_ids_seed_videos, n)

# Saving the lists into a csv file
df_related_videos = pd.DataFrame(lst_related_videos,
                                     columns =['Video ID', 'Video URL', 'Video Title',
                                               'Channel ID', 'Channel Name', 'Seed Video ID'])



# SAVING THE RELATED VIDEO IDs INTO A CSV
df_related_videos.to_csv(output_file_path + output_file_name + "-related(from seeds).csv")
    

# -------------------------------------------------------

# Provide the YouTube video ID
video_id = "4MymINGlSqo"
related_videos = get_related_videos(video_id, 5)

lst_related_videos = []
for v in related_videos:
    lst_related_videos.append(v) 
    #print(v)
df_related_videos = pd.DataFrame(lst_related_videos,
                                     columns =['Video ID', 'Video URL', 'Video Title',
                                               'Channel ID', 'Channel Name', 'Seed Video ID'])
