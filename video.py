from utils import api_client
import os
from googleapiclient.discovery import build

class Video:
	def __init__(self, id_: str, video_name="Default"):
		self.__id = id_

	@property
	def title(self):
		video_info = Video.get_service().videos().list(id=self.__id, part="snippet").execute()
		return video_info['items'][0]['snippet']['title']

	@property
	def likes(self):
		video_info = Video.get_service().videos().list(id=self.__id, part="statistics").execute()
		return video_info['items'][0]['statistics']['likeCount']

	@property
	def views(self):
		video_info = Video.get_service().videos().list(id=self.__id, part="statistics").execute()
		return video_info['items'][0]['statistics']['viewCount']

	@classmethod
	def get_service(cls):
		api_key: str = os.getenv('YT_API')
		youtube = build('youtube', 'v3', developerKey=api_key)
		return youtube

	def __str__(self):
		return f'{self.title}'


class PLVideo(Video):
	def __init__(self, id_, playlist_id):
		super().__init__(id_)
		self.video_id = id_
		self.playlist_id = playlist_id

	@property
	def pl_title(self):
		playlist = PLVideo.get_service().playlists().list(id=self.playlist_id, part='snippet').execute()
		return playlist['items'][0]['snippet']['title']

	def __str__(self):
		return f'{self.title} ({self.pl_title})'
