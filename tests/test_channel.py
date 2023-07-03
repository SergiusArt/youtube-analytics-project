import pytest
from src.channel import Channel


@pytest.fixture
def class_channel():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


def test_repr(class_channel):
    assert class_channel.__repr__() == f'ID канала = UC-OVMPlMA3-YCIeg4z5z23A, API ключ = True'


def test_init(class_channel):
    assert class_channel.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'
    assert class_channel.id == "UC-OVMPlMA3-YCIeg4z5z23A"
    assert class_channel.title == "MoscowPython"
    assert class_channel.description == "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\n" \
                                        "Присоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)"
    assert class_channel.custom_url == "@moscowdjangoru"
    assert class_channel.url == 'https://www.youtube.com/@moscowdjangoru'
    assert class_channel.subscriber_count > 0
    assert class_channel.video_count > 0
    assert class_channel.view_count > 0
