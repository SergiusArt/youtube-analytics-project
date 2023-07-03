import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.__channel_id = channel_id
        self.channel = Channel.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()

        self.id = self.channel['items'][0]['id']
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.custom_url = self.channel['items'][0]['snippet']['customUrl']
        self.url = f'https://www.youtube.com/{self.custom_url}'
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self):
        """
        Позволяет обращаться к channel ID как к аргументу
        """

        return self.__channel_id

    @classmethod
    def get_service(cls):
        """ Возвращает объект для работы с TouTube API"""

        return build('youtube', 'v3', developerKey=cls.api_key)

    def to_json(self, path):
        """ Сохраняет в файл значения атрибутов экземпляра """
        data = self.__dict__
        del data['channel']
        with open(path, 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def __repr__(self):
        """ Выводит ID канала к которому привязан класс и наличие соединения по АПИ"""

        return f'ID канала = {self.channel_id}, API ключ = {len(self.api_key) > 1}'

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        print(self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute())
