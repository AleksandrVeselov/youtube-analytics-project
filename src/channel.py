import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    API_KEY: str = os.getenv('YOUTUBE_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=Channel.API_KEY)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def print_playlists_info(self) -> None:
        playlists = self.youtube.playlists().list(channelId=self.channel_id,
                                             part='contentDetails,snippet',
                                             maxResults=50,
                                             ).execute()
        for playlist in playlists['items']:
            print(playlist)
            print()

    def print_info_about_playlist(self, playlist_id) -> None:
        playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        print(json.dumps(playlist_videos, indent=2, ensure_ascii=False))

    def print_info_about_video(self, video_id):
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        print(json.dumps(video_response, indent=2, ensure_ascii=False))


channel_id = 'UCMcC_43zGHttf9bY-xJOTwA'  # egoroff_channel

channel = Channel(channel_id)

channel.print_info()
channel.print_playlists_info()

playlist_id = 'PLQAt0m1f9OHvyjJNjZK_unnLwMOXPTja8'  # ООП

channel.print_info_about_playlist(playlist_id)

video_id = "8sIUlyQh2ks"

channel.print_info_about_video(video_id)
