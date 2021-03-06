import pytest
from models.player import Player

from ..fixtures import tim


def test_class_definition(tim):
    """ 010A The class is called Player"""
    assert type(tim) == Player


def test_player_arguments():
    """ 020A The constructor should have 1 argument(TypeError otherwise)"""
    with pytest.raises(TypeError):
        p = Player(["s"], ["h"])


def test_player_attributes(tim):
    """ 020B Player’s attributes are set to the original argument when it is valid"""
    assert tim._backpack == ["h", "t"]


def test_player_backpack(tim):
    """ 030A The backpack property get the backpack values"""
    assert tim.backpack == ["h", "t"]


def test_player_wrong_backpack_type():
    """ 030B The backpack property checks that the items are a list (TypeError otherwise)"""
    with pytest.raises(TypeError):
        t = Player({"h": -1, "s": 3})


def test_player_properties(tim):
    """ 030C The types of all properties of player class are property"""
    assert type(tim.__class__.backpack) == property


def test_pickup_arguments():
    """ 040A The pickup method should have 1 argument(TypeError otherwise)"""
    p = Player([])
    with pytest.raises(TypeError):
        p.pickup("s", "h")


def test_pickup_wrong_item_type():
    """ 040B The pickup method checks that the item is a string(TypeError otherwise)"""
    p = Player([])
    with pytest.raises(TypeError):
        p.pickup(3)


def test_pickup_value():
    """ 040C The The pickup method checks that the picked item is added to the backpack"""
    t = Player([])
    t.pickup("h")
    assert t.backpack == ["h"]
