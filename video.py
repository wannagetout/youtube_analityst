from mixin import MixinYT


class Video(MixinYT):

	def __init__(self, id_):
		self.id_ = id_
		video_info_snippet = Video.get_service().videos().list(id=self.id_, part="snippet").execute()
		video_info_stat = Video.get_service().videos().list(id=self.id_, part="statistics").execute()
		try:
			self.title = video_info_snippet['items'][0]['snippet']['title']
			self.likes = video_info_stat['items'][0]['statistics']['likeCount']
			self.views = video_info_stat['items'][0]['statistics']['viewCount']
		except:
			self.title = None
			self.likes = None
			self.views = None

	def __str__(self):
		return f'{self.title}'


class PLVideo(Video):
	def __init__(self, id_, pl_id):
		super().__init__(id_)
		self.pl_id = pl_id

	@property
	def pl_title(self):
		playlist = PLVideo.get_service().playlists().list(id=self.pl_id, part='snippet').execute()
		return playlist['items'][0]['snippet']['title']

	def __str__(self):
		return f'{self.title} ({self.pl_title})'


class Playlist(MixinYT):
	def __init__(self, id_):
		self.id_ = id_

	@property
	def title(self):
		playlist = Playlist.get_service().playlists().list(id=self.id_, part='snippet').execute()
		return playlist['items'][0]['snippet']['title']

	@property
	def url(self):
		return f'https://www.youtube.com/playlist?list={self.id_}'

	def video_list(self):
		playlist = Playlist.get_service().playlistItems().list(
			playlistId=self.id_,
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
