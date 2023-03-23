# -*- coding: utf-8 -*-
from src import channel
from googleapiclient.discovery import build
import os


class Video:

    def __init__(self, video_id):
        """Инициализация атрибутов класса"""

        # Получение информации о видео
        self.video_response = self.get_info(video_id)

        # Заполнение атрибутов соответствующими данными
        self.video_id = video_id
        self.video_title = self.video_response['items'][0]['snippet']['title']
        self.video_url = f'https://www.youtube.com/video/{self.video_id}'
        self.views_count = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count = self.video_response['items'][0]['statistics']['likeCount']

    @staticmethod
    def get_info(video_id):
        """Получение информации о видео"""

        API_KEY: str = os.getenv('YOUTUBE_API_KEY')
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id=video_id
                                       ).execute()
        return video_response

    def __str__(self):
        return self.video_title


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        """Инициализация атрибутов класса"""
        super().__init__(video_id)
        self.playlist_id = playlist_id






