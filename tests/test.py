from channel import Channel
from video import Video, PLVideo, Playlist

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


def test_video():
	video = Video('BBotskuyw_M')
	assert video.title == 'Пушкин: наше все?'

	broken_video = Video('D5SKbtnK54')
	assert broken_video.title == None
	assert broken_video.id_ == 'D5SKbtnK54'

def test_pl_video():
	pl_video = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
	assert pl_video.title == 'Пушкин: наше все?'
	assert pl_video.pl_title == 'Литература'


def test_Playlist():
	pl = Playlist('PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
	assert pl.url == 'https://www.youtube.com/playlist?list=PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD'
	assert pl.show_best_video() == 'https://youtu.be/1ot9xIG9lKc'
