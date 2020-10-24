import pytest

from models.player import Player


@pytest.fixture
def tim():
    
    return Player(["h","t"])