from src.channel import Channel


class Video(Channel):

    def __init__(self, id_video: str):

        try:
            self.id_video = id_video

            self.video_info = Channel.get_service().videos().list(id=id_video, part='snippet,statistics').execute()

            self.title = self.video_info['items'][0]['snippet']['title']
            self.url_video = f'https://youtu.be/{self.id_video}'
            self.view_count = self.video_info['items'][0]['statistics']['viewCount']
            self.like_count = self.video_info['items'][0]['statistics']['likeCount']
        except Exception:
            self.id_video = id_video
            self.video_info = None
            self.title = None
            self.url_video = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        """
        Заголовок видео
        """

        return self.title


class PLVideo(Video):
    def __init__(self, id_video: str, id_playlist: str):
        super().__init__(id_video)
        self.id_playlist = id_playlist

        self.playlist_info = Channel.get_service().playlistItems().list(playlistId=self.id_playlist,
                                                                        part='contentDetails', maxResults=50,).execute()

        self.title_video = Video(id_video).title
        self.url_video = None
        self.view_count = Video(id_video).view_count

    def __str__(self):
        """
        Заголовок видео
        """

        return self.title

