from channel import Channel


channel_id_1 = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
channel_id_2 = 'UC1eFXmJNkjITxPFWTy6RsWg'

ch1 = Channel(channel_id_1)
ch2 = Channel(channel_id_2)


def test_more_than():
	assert ch1.__gt__(ch2) is True


def test_less_than():
	assert ch1.__lt__(ch2) is False


def test_add():
	assert (ch1 + ch2) == ch1.subscribers_count + ch2.subscribers_count