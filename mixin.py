import os
from googleapiclient.discovery import build


class MixinYT:

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube
