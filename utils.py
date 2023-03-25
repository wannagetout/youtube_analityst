import os

from googleapiclient.discovery import build


API_KEY: str = os.environ.get('YT_API')


def api_client():
	youtube = build('youtube', 'v3', developerKey=API_KEY)
	return youtube
