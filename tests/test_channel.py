import pytest
from src.channel import Channel


@pytest.fixture
def class_channel():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


def test_repr(class_channel):
    assert class_channel.__repr__() == f'ID канала = UC-OVMPlMA3-YCIeg4z5z23A, API ключ = True'
