# -*- coding: utf-8 -*-

"""
This script splits given videos into 1 min scenes

INPUT
    - A list of the Video IDs that will serve as the seeds
OUTPUT
    - A directory with the related videos and a csv file with the data of the related videos

NOTES:
    - Be careful to be on path: 
        D:\itzel\PhD Computer Science\github-codes\dcc-hsdvmi-video-dataset\2.1 video segments
    - It is required to install Ffmpeg
    - The limit video duration could be specified

@author: itzel
last-edited: 23-06-27
"""
import os
import subprocess
import ffmpeg

def get_video_duration(input_video):
    probe = ffmpeg.probe(input_video)
    video_info = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
    duration = float(video_info['duration'])
    duration_minutes = round(duration / 60, 2)
    return duration_minutes

def split_video(input_video, output_dir):
    #print(input_video)
    file = input_video.split('/')[-1]
    result = subprocess.run(["ffmpeg", "-i", input_video,"-map","0", "-c", "copy", "-f", "segment", "-segment_time", "60","-reset_timestamps", "1", output_dir+"/"+file.split(".")[0]+".%02d."+file.split(".")[-1]],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

def split_videos_from_directory(input_dir, output_dir, max_time):
    print("Input Dir :", input_dir)
    print("Output Dir :", output_dir) 
    #print(max_time)
    lst_contents = os.listdir(input_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    i = 0
    for video in lst_contents:
        video_file = input_dir +"/"+ video 
        try:
            duration_minutes = get_video_duration(video_file)
        except:
            duration_minutes = -1
        if duration_minutes > 0 and duration_minutes <= max_time:
            i = i + 1
            print(str(i)+"/"+str(len(lst_contents) -1), f"Video duration: {duration_minutes} minutes")
            split_video(video_file, output_dir)
        else:
            continue
            
"""
The following variables correspond to:
- source_dir: directory path were the subsets of download videos are saved
    
- output_dir: directory path were the video scenes are going to be stored in the format
            video_id.number_of_scene.extension
"""
videos_source_dir= "../1.2 YouTube retrieved videos/1.2.2 YT videos (downloaded)/" 
lst_content_source_dir = os.listdir(videos_source_dir)

output_dir="./2.1.1 video segments/"
if not os.path.exists(output_dir):
   os.makedirs(output_dir)

"""
PROCESS ONE SPECIFIC DIRECTORY
"""
#input_dir_path = input("Input Directory path to process: ")  
i = 2
input_dir_path = videos_source_dir + lst_content_source_dir[i]

output_dir_path = output_dir + lst_content_source_dir[i] +"-segments/"
time_limit_minutes = 20

split_videos_from_directory(input_dir_path, output_dir_path, time_limit_minutes)

"""
PROCESS ALL SUB DIRECTORIES IN A SOURCE DIRECTORY
"""

for directory in lst_content_source_dir[3:]:
    print("------------------------------------------------------------------")
    input_dir_path = videos_source_dir + directory
    output_dir_path = output_dir + directory +"-segments/"
    time_limit_minutes = 20
    
    split_videos_from_directory(input_dir_path, output_dir_path, time_limit_minutes)