# -*- coding: utf-8 -*-
"""
This script creates batches of n videos given a list of videos

root dir:
    \dcc-hsdvmi-video-dataset\3.1 video segments to batches

@author: itzel
last edited: 2023-09-16
"""
import os
import random
import csv

# 1 specify the directory path were the video segments are
dir_video_segments = "../2.1 video segments/2.1.1 video segments/"
#print(os.listdir(dir_video_segments))

# only consider the relevant, related and playlist videos to join into the pool of videos
lst_ids = []
lst_pool = []
for d in os.listdir(dir_video_segments):
    if "relevant" in d or "related" in d or "playlist" in d:
        if "relevant" in d:
            source = "rt"
        elif "related" in d:
            source = "rd"
        elif "playlist" in d:
            source = "pl"
        print(len(os.listdir(dir_video_segments + d)), d)
        # each video into the pool (video_id, source, full_source)
        for v in os.listdir(dir_video_segments + d):
            if v not in lst_ids:
                lst_ids.append(v) # avoid repeated video files
                lst_pool.append((v, source, d))
            else:
                continue

# bulding the batches with random videos
def divide_into_batches_of_n_videos(lst, n):
    random.shuffle(lst)
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

n_videos_per_batch = 250
batches_random = list(divide_into_batches_of_n_videos(lst_pool, n_videos_per_batch))

# 2 save each batch into a csv file
dir_batch_csv_files = './3.1.1 batch csv files/'
if not os.path.exists(dir_batch_csv_files):
    # If it doesn't exist, create the directory
    os.makedirs(dir_batch_csv_files)

dir_batch_files = './3.1.1 batch files/'
if not os.path.exists(dir_batch_files):
    # If it doesn't exist, create the directory
    os.makedirs(dir_batch_files)

for i, batch in enumerate(batches_random):
    # full info (video_id, source, full_source)
    file_path = dir_batch_csv_files+f'info_batch_{i+1}.csv'
    headers = ['video_id', 'source', 'full_source']
    with open(file_path, mode='w',  encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for triplet in batch:
            writer.writerow({'video_id': triplet[0], 'source': triplet[1], 'full_source': triplet[2]})
    # just the ids (video_id)
    file_path = dir_batch_files+f'batch_{i+1}.csv'
    with open(file_path, mode='w',  encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for triplet in batch:
            writer.writerow([triplet[0]])
        
    print(f'Batch_{i+1}', len(batch), file_path)
        
