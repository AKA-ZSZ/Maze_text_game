import pytest
from unittest.mock import mock_open, patch
from models.maze import Maze

@pytest.fixture
def my_maze():
    return Maze()

def test_class_definition(my_maze):
    assert type(my_maze) == Maze

def test_structure_attribute(my_maze):
    assert type(my_maze.structure) == list

def test_maze_properties(my_maze):
    assert type(my_maze.__class__.structure) == property
    assert type(my_maze.__class__.movements_player) == property
    assert type(my_maze.__class__.items) == property
    assert type(my_maze.__class__.locations) == property
    assert type(my_maze.__class__.player) == property


@patch('builtins.open', mock_open(read_data="   XXXX\n   XX  "))
def test_load_all_from_file(my_maze):
    my_maze._load_all_from_file()
    assert len(my_maze.structure) == 2
    assert my_maze.check_position(0, 2)
    assert my_maze.check_position(0, 5) == False

@patch('builtins.open', mock_open(read_data="   XXXX\n   XX   "))
def test_find_random_spot(my_maze):
    my_maze._load_all_from_file()
    row_value, col_value = my_maze.find_random_spot()
    assert my_maze.check_position(row_value, col_value)

@patch('builtins.open', mock_open(read_data="   XXXX\nT   XX  "))
def test_is_item(my_maze):
    my_maze._load_all_from_file()
    assert my_maze.is_item(1, 0)

@patch('builtins.open', mock_open(read_data="   XXXX\nT P  XX  "))
def test_move_player(my_maze):
    my_maze._load_all_from_file()
    my_maze.move_player(1, 0)
    assert my_maze.movements_player == [1, 0]

# def test_is_exit(my_maze):
#     my_maze.is_exit





    
