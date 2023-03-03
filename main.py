from channel import Channel


if __name__ == '__main__':

	channel_id_1 = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
	channel_id_2 = 'UC1eFXmJNkjITxPFWTy6RsWg'

	ch1 = Channel(channel_id_1)
	ch2 = Channel(channel_id_2)

	print(ch1)
	print(ch2)
	print(ch1 > ch2)
	# print(ch1.subscribers_count)
	# print(ch2.subscribers_count)
	print(ch1 + ch2)
