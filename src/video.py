from src import channel


class Video(channel.Channel):
    """Класс для видео"""

    def __init__(self, video_id):
        """Инициализация атрибутов класса"""

        # Получение информации о видео
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id=video_id
                                       ).execute()

        # Заполнение атрибутов соответсвующими данными
        self.video_id = video_id
        self.video_title = self.video_response['items'][0]['snippet']['title']
        self.video_url = f'https://www.youtube.com/video/{self.video_id}'
        self.views_count = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count = self.video_response['items'][0]['statistics']['likeCount']



