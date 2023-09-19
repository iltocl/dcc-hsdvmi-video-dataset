# A Dataset for Hate Speech Detection in Videos 

This is the documentation of the construction of our **Mexican Spanish Video Dataset**. 
A dataset aimed to be used for the **hate speech detection task**.

- [A Dataset for Hate Speech Detection in Videos](#a-dataset-for-hate-speech-detection-in-videos)
   - [Summary](#summary)
   - [Getting Started](#getting-started)
   - [Citation](#citation)
   - [Acknowledgments](#acknowledgments)
   - [Media Coverage](#media-coverage)

# Summary







The construction of the dataset consists of the following phases:

###  1. Collecting the videos (In progress...)
- [x] 1.1 Lists of hate speech (HS) words to be used as seeds
   - SRE list (56 words)
   - hatebase list (29 words)
- [x] 1.2 YouTube retrieved videos
   
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
