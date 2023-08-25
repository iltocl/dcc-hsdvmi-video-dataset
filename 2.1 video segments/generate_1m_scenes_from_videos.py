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

def get_video_duration(input_file):
    probe = ffmpeg.probe(input_file)
    video_info = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
    duration = float(video_info['duration'])
    duration_minutes = round(duration / 60, 2)
    return duration_minutes

def split_video(input_file, output_dir):
    #print(input_file)
    file = input_file.split('/')[-1]
    result = subprocess.run(["ffmpeg", "-i", input_file,"-map","0", "-c", "copy", "-f", "segment", "-segment_time", "60","-reset_timestamps", "1", output_dir+"/"+file.split(".")[0]+".%02d."+file.split(".")[-1]],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

def split_videos_from_dir(input_dir_path, output_dir, time_limit):
    #print(input_dir_path, output_dir, time_limit)
    lst_contenido = os.listdir(input_dir_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for video in lst_contenido:
        print(video)
        try:
            duration_minutes = get_video_duration(input_dir_path+video)
        except:
            duration_minutes = -1
                
        if duration_minutes>0 and duration_minutes <= time_limit:
            print(f"Video duration: {duration_minutes} minutes")
            split_video(sub_dir_path+video, output_dir)
        else:
            continue
            
"""
The following variables correspond to:
- source_dir: directory path were the subsets of download videos are saved
    
- output_dir: directory path were the video scenes are going to be stored in the format
            video_id.number_of_scene.extension
"""
source_dir= "../1.2 YouTube retrieved videos/1.2.2 YT videos (downloaded)/" 
lst_content_source_dir = os.listdir(source_dir)

time_limit_minutes = 20
output_dir="./videos-to-scenes/"

if not os.path.exists(output_dir):
   os.makedirs(output_dir)

"""
PROCESS ONE SPECIFIC DIRECTORY
"""
i = 0
sub_dir_name = lst_content_source_dir[i]+"/"
sub_dir_path= source_dir + sub_dir_name
print(sub_dir_path)
#lst_contenido = os.listdir(sub_dir_path)
split_videos_from_dir(sub_dir_path, output_dir+sub_dir_name, time_limit_minutes)

"""
PROCESS ALL SUB DIRECTORIES IN A SOURCE DIRECTORY
"""
for directory in lst_content_source_dir:
    sub_dir_path = source_dir + directory + "/"
    #print(sub_dir_path)
    print(output_dir + directory + "/")
    split_videos_from_dir(sub_dir_path, output_dir + directory + "/", time_limit_minutes)