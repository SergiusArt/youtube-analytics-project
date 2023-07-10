from src.channel import Channel


class Video(Channel):

    def __init__(self, id_video: str):
        self.id_video = id_video

        self.video_info = Channel.get_service().videos().list(id=id_video, part='snippet,statistics').execute()

        self.title_video = self.video_info['items'][0]['snippet']['title']
        self.url_video = None
        self.view_count = self.video_info['items'][0]['statistics']['viewCount']
        self.like_count = self.video_info['items'][0]['statistics']['likeCount']

    def __str__(self):
        """
        Заголовок видео
        """

        return self.title_video


class PLVideo(Video):
    def __init__(self, id_video: str, id_playlist: str):
        super().__init__(id_video)
        self.id_playlist = id_playlist

        self.playlist_info = Channel.get_service().playlistItems().list(playlistId=self.id_playlist,
                                                                        part='contentDetails', maxResults=50,).execute()

        self.title_video = Video(id_video).title_video
        self.url_video = None
        self.view_count = Video(id_video).view_count

    def __str__(self):
        """
        Заголовок видео
        """

        return self.title_video

