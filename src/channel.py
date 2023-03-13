import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    API_KEY: str = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.__channel_id = channel_id
        self.channel = Channel.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.subscribers_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.views_count = self.channel['items'][0]['statistics']['viewCount']

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с API вне класса"""
        return cls.youtube

    @property
    def channel_id(self):
        """Свойство для обращения к приватному атрибуту __channel_id"""
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, file_name: str) -> None:
        """Запись информации о канале в file_name.json"""
        with open(file_name, 'w') as json_file:
            json.dump(self.channel, json_file, ensure_ascii=False)


