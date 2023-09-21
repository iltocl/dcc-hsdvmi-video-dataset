# A Dataset for Hate Speech Detection in Videos 

This repository hosts the documentation of the construction of our **Mexican Spanish Video Dataset**. 
A dataset aimed to be used for the **hate speech detection task**.

- [A Dataset for Hate Speech Detection in Videos](#a-dataset-for-hate-speech-detection-in-videos)
   - [Summary](#summary)
   - [Getting Started](#getting-started)
   - [Citation](#citation)
   - [Acknowledgments](#acknowledgments)
   - [Media Coverage](#media-coverage)

# Summary
The hate speech detection task has been gaining interest in recent years. Existing methods address the task for English language-based resources. Then, a lack of experimentation in other languages is notable not only by the language itself but also by the limited availability of datasets.

In this regard, we present our _Mexican Spanish Video Dataset_, which is built by collecting YouTube videos with possible hate speech content. 

<img src="hsdvmi-dataset-creation.PNG" alt="" width="900">

The built up of the dataset consists of:
- Collecting videos (from YouTube and with possible relation to hate speech content)
- Annotating the dataset 
- Formalizing the dataset 

# Getting Started

## Code Structure
```
├── 1.1 hate speech words lists            # csv files of hate speech related words
├── 1.2 YouTube retrieved videos           # filtering and downloading scripts and videos
│   ├── 1.2.1 YT videos (lists of IDs)     # csv files of filtered YT videos
│   ├── 1.2.2 YT videos (downloaded)
│   ├── download_videos_youtube.py
│   ├── download_videos_youtube_specific_playlist.py
│   ├── filter_lst_videos_from_youtube.py
│   ├── filter_lst_videos_using_video_seeds.py
├── 2.1 video segments                     # segmentating the previously downloaded videos
│   ├── 2.1.1 video segments
│   ├── generate_1m_scenes_from_videos.py
├── 3.1 video segments to batches
│   └── generate_video_batches.py
└── README.md
```

##  1. Collecting the videos 
First, videos are filtered and downloaded from YouTube (YT) platform using a hate speech (HS) related word lists as seeds. Two lists were used:
1. A list based on expressions/terms we should avoid in order to use inclusive and non-sexist language. This list is based on the _Guía de lenguaje incluyente y no sexista_ published by the _Secretaría de Relaciones Exteriores_ and include 56 words.
2. A list based on terms catalogued as offensive in the mexican context. This list is based on the terms obtained by the _hatebase_ website and includes 29 words.

   
   First, videos are retrieved using a hate speech words list. Second, relevant videos are manually chosen as relevant from the original retrieved ones. Third, using the relevant videos previously selected these became seeds to retrieve more similar videos. Also, retrieving videos considering specific YouTube channels and/or playlists is considered.
   - [x] 1.2.1 YT videos (lists of IDs). This folder contains lists of YouTube video IDs filtered by using the hate speech lists.   
   - [x] 1.2.2 YT videos (downloaded). This folder contains the downloaded videos, organized by:
      - [x] Folders of downloaded (dwnld_) videos directly from YouTube using the lists of IDs in 1.2.1
      - [x] Folders of relevant (-relevant) videos manually selected from the original downloaded ones (these videos will serve as seeds to search for similar ones)
      - [x] Folders of related (-related) videos that were retrieved using the relevant ones as seeds
      - [x] Folders with videos retrieved from specific manually identified channels or playlists (-channel-channelname, -playlist-playlistname)

### 2. Videos dataset
Once enough videos are retrieved/downloaded it is necessary to segment each one to fragments of 1-minute length.
- [x] 2.1 Video Segments

### 3. Video segments to batches
To build the pool of videos that will be labeled as the dataset only the relevant, related and playlist ones are considered. This because:
- relevant: include videos manually selected from the original filtering from YouTube
- related: include videos retrieved by using the relevant ones as seeds
- playlist: include videos from playlists manually identified from certain YouTube channels
Then, this pool of videos is chunked into batches of n number of videos in order to facilitate the annotation process. These batches are randomly built.
- [x] 3.1 video segments to batches

### 4. Annotating the videos
The annotation webapp built for this project can be accessed through the following link.
- [ ] https://github.com/iltocl/hsdvmi-video-annotation-webapp.git
   
### 5. Formalizing the dataset
- [ ] train (%)
- [ ] test (%)
