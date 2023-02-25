from channel import Channel


if __name__ == '__main__':

	channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'

	a = Channel(channel_id)
	print(a.title)
	print(a.__dict__)
	print(a.channel_info())
	print(a.get_service())
	a.to_json('name')
	print(a.title)