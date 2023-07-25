from src.channel import Channel
import datetime


class PlayList:

    def __init__(self, id_playlist):
        self.playlist_info = Channel.get_service().playlistItems().list(
            playlistId=id_playlist, part='contentDetails,snippet', maxResults=50).execute()

        self.channel_id = self.playlist_info['items'][0]['snippet']['channelId']

        self.channel_info = Channel.get_service().playlists().list(
            channelId=self.channel_id, part='contentDetails,snippet', maxResults=50).execute()

        self.id_playlist = id_playlist

        for item in self.channel_info['items']:
            if item['id'] == self.id_playlist:
                self.title = item['snippet']['title']

        self.url = f'https://www.youtube.com/playlist?list={self.id_playlist}'

    @property
    def total_duration(self):
        """
        Показывает общее время всех видео в плейлисте
        """

        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_info['items']]

        video_response = Channel.get_service().videos().list(part='contentDetails,statistics',
                                                             id=','.join(video_ids)
                                                             ).execute()
        # printj(video_response)

        all_time = []
        time_delta = datetime.datetime(1900, 1, 1, 0, 0, 0)

        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_duration = video['contentDetails']['duration']
            if 'S' not in (iso_duration):
                iso_duration += '0S'
            time_obj = datetime.datetime.strptime(iso_duration, "PT%MM%SS")
            all_time.append(datetime.timedelta(hours=time_obj.hour, minutes=time_obj.minute, seconds=time_obj.second))

        for i in range(len(all_time)):
            time_delta = time_delta + all_time[i]
        return datetime.timedelta(hours=time_delta.hour, minutes=time_delta.minute, seconds=time_delta.second)

    def show_best_video(self):
        """
        Показывает лучшее видео по количеству лайков
        """

        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_info['items']]

        video_response = Channel.get_service().videos().list(
            part='contentDetails,statistics', id=','.join(video_ids)).execute()

        best_count = 0
        best_video = ''
        i = 0

        for video in video_response['items']:
            if int(video['statistics']['likeCount']) > best_count:
                best_count = int(video['statistics']['likeCount'])
                best_video = video_ids[i]
                i += 1

        return f'https://youtu.be/{best_video}'
