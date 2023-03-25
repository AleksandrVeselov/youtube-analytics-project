# -*- coding: utf-8 -*-
import os
from googleapiclient.discovery import build
from src import video
from datetime import timedelta
import isodate


class PlayList:
    """Класс для представления плейлиста"""
    __API_KEY: str = os.getenv('YOUTUBE_API_KEY')
    __youtube = build('youtube', 'v3', developerKey=__API_KEY)

    def __init__(self, playlist_id: str) -> None:
        self.playlist_id = playlist_id  # ИД плейлиста
        self.playlist_data = self.get_data(playlist_id)  # данные о плейлисте
        self.title = self.playlist_data['items'][0]['snippet']['title']  # название плейлиста
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'  # ссылка на плейлист
        self.playlist_videos = self.get_videos()  # список видео плейлиста (экземпляров класса видео)
        self.__total_duration = self.get_total_duration()  # общая продолжительность всех видео из плейлиста

    @property
    def total_duration(self):
        return self.__total_duration

    def get_data(self, playlist_id: str):
        """Получаем данные о плейлисте"""

        playlist_info = PlayList.__youtube.playlists().list(id=playlist_id,
                                                            part='contentDetails,snippet',
                                                            maxResults=50,
                                                            ).execute()

        return playlist_info

    def get_total_duration(self):
        """Нахождение общей продолжительности всех видео из плейлиста"""

        time = timedelta()  # Начальная длительность

        for video_id in self.playlist_videos:
            print(video_id.duration)
            time += isodate.parse_duration(video_id.duration)
        return time

    def get_videos(self) -> list:
        """Создание списка из экземпляров класса Video"""

        videos = []  # Список ИД всех видео из плейлиста (изначально пуст)
        playlist_videos = PlayList.__youtube.playlistItems().list(playlistId=self.playlist_id,
                                                                  part='contentDetails',
                                                                  maxResults=50,
                                                                  ).execute()

        # Создаем экземпляр класса Video и добавляем его в список
        for playlist_video in playlist_videos['items']:
            videos.append(video.Video(playlist_video['contentDetails']['videoId']))
        return videos

    def show_best_video(self) -> str:
        """
        Нахождение видео с максимальным количеством лайков и возврещение ссылки на него
        """

        best_video = max(self.playlist_videos, key=lambda x: int(x.like_count))
        return best_video.video_url





