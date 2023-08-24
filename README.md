# dcc-hsdvmi-video-dataset
# Title: Hate Speech Detection in Videos using Multimodal Information

@author: itzel

Last edited: 2023-06-09

This repository documents the construction of a **Mexican Spanish Video Dataset** that aims to be used for the **hate speech detection task** in computer science.

The construction of the dataset consists of the following phases:

###  1. Collecting the videos (In progress...)
- [x] 1.1 Lists of hate speech (HS) words to be used as seeds
   - SRE list (56 words)
   - hatebase list (29 words)
- [x] 1.2 YouTube retrieved videos
   
   First, videos are retrieved using a hate speech words list. Second, relevant videos are manually chosen as relevant from the original retrieved ones. Third, using the relevant videos previously selected these became seeds to retrieve more similar videos. Also, retrieving videos considering specific YouTube channels and/or playlists is considered.
   - 1.2.1 YT videos (lists of IDs). This folder contains lists of YouTube video IDs filtered by using the hate speech lists.   
   - 1.2.2 YT videos (downloaded). This folder contains the downloaded videos, organized by:
      - Folders of downloaded (dwnld_) videos directly from YouTube using the lists of IDs in 1.2.1
      - Folders of relevant (_rlvnt) videos manually selected from the original downloaded ones (these videos will serve as seeds to search for similar ones)
      - Folders of similar (_smlr) videos that were retrieved using the relevant ones as seeds
      - Folders with videos retrieved from specific manually identified channels or playlists

### 2. Videos dataset
Once enough videos are retrieved/downloaded it is necessary to segment each one to fragments of 1-minute length.
- [ ] 2.1 Video Segments
 
### 3. Annotating the videos
   3.1
### 4. Formalizing the dataset
