from utils import api_client
import os
from googleapiclient.discovery import build

from mixin import MixinYT
from datetime import datetime, time, timedelta


class Video(MixinYT):
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

	def __str__(self):
		return f'{self.title}'


class PLVideo(Video):
	def __init__(self, id, pl_id):
		super().__init__(id)
		self.pl_id = pl_id

	@property
	def pl_title(self):
		playlist = PLVideo.get_service().playlists().list(id=self.pl_id, part='snippet').execute()
		return playlist['items'][0]['snippet']['title']

	def __str__(self):
		return f'{self.title} ({self.pl_title})'


class Playlist(MixinYT):
	def __init__(self, id):
		self.id = id


	@property
	def title(self):
		playlist = Playlist.get_service().playlists().list(id=self.id, part='snippet').execute()
		return playlist['items'][0]['snippet']['title']

	@property
	def url(self):
		return f'https://www.youtube.com/playlist?list={self.id}'

	def video_list(self):
		playlist = Playlist.get_service().playlistItems().list(
			playlistId=self.id,
			part="contentDetails",
			maxResults=50
		).execute()

		video_list = []
		for item in playlist['items']:
			video_list.append(item['contentDetails']['videoId'])
		return video_list

	def show_best_video(self):
		video_list = self.video_list()
		best_video = ''
		likes = 0
		for item in video_list:
			video = Video(item)
			if int(video.likes) > likes:
				likes = int(video.likes)
				best_video = item
		return f'https://youtu.be/{best_video}'


pl=Playlist('PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
print(pl.url)
print(pl.video_list())
print(pl.show_best_video())
