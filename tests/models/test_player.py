import pytest
from unittest.mock import mock_open, patch
from models.player import Player

from ..fixtures import tim

def test_player_attributes(tim):
    assert tim.backpack==["h","t"]

def test_player_backpack_type():
    with pytest.raises(TypeError):
        t = Player({"h":-1,"s":3})

def test_player_properties(tim):
    assert type(tim.__class__.backpack) == property

def test_pickup_value():
    t=Player([])
    t.pickup("h")
    assert t.backpack==["h"]
    


# @patch('builtins.open', mock_open(read_data='Tim,A01209697,20,100,90'))
# def test_load_all():
#     students = Student.load_all_from_file()
#     assert len(students) == 1
#     assert students[0].name == 'Tim'
#     assert students[0].gpa == 70
