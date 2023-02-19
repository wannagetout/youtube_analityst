import json

from utils import api_client


class Channel:

	def __init__(self, id_: object):
		self.id_ = id_

	def get_channel(self):
		client = api_client()
		channel = client.channels().list(id=self.id_, part='snippet, statistics').execute()
		channel = json.dumps(channel, indent=2, ensure_ascii=False)
		return channel
