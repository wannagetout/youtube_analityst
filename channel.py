import json

from mixin import MixinYT
from utils import api_client


class Channel(MixinYT):

	def __init__(self, id_: object):
		self.__id_ = id_

	def channel_info(self):
		client = api_client()
		channel = client.channels().list(id=self.__id_, part='snippet, statistics').execute()
		channel = json.dumps(channel, indent=2, ensure_ascii=False)
		return json.loads(channel)

	@property
	def title(self):
		return self.channel_info()['items'][0]['snippet']['title']

	@property
	def description(self):
		return self.channel_info()['items'][0]['snippet']['description']

	@property
	def url(self):
		return self.channel_info()['items'][0]['thumbnails']['url']

	@property
	def subscribers_count(self):
		return int(self.channel_info()['items'][0]['statistics']['subscriberCount'])

	@property
	def video_count(self):
		return self.channel_info()['items'][0]['statistics']['videoCount']

	@property
	def views_count(self):
		return self.channel_info()['items'][0]['statistics']['viewCount']

	def to_json(self, file_name):
		with open(file_name+'.json', 'w', encoding='utf-8') as file:
			info = json.dumps(self.channel_info())
			for line in info:
				file.write(line)

	def __gt__(self, other):
		return self.subscribers_count > other.subscribers_count

	def __lt__(self, other):
		return self.subscribers_count < other.subscribers_count

	def __add__(self, other):
		return self.subscribers_count + other.subscribers_count

	def __repr__(self):
		return f'Youtube-канал: {self.title}'
