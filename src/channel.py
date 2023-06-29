import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.api_key = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def __repr__(self):
        """ Выводит ID канала к которому првязан класс и наличие соединения по АПИ"""
        return f'ID канала = {self.channel_id}, API ключ = {len(self.api_key) > 1}'

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute())
