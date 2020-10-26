import pytest
from models.player import Player

from ..fixtures import tim

def test_player_attributes(tim):
    assert tim.backpack==["h","t"]

def test_player_wrong_backpack_type():
    with pytest.raises(TypeError):
        t = Player({"h":-1,"s":3})

def test_player_properties(tim):
    assert type(tim.__class__.backpack) == property

def test_pickup_value():
    t=Player([])
    t.pickup("h")
    assert t.backpack==["h"]

