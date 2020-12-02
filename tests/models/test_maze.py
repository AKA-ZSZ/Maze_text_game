import pytest
from unittest.mock import mock_open, patch
from models.maze import Maze


@pytest.fixture
def my_maze():
    return Maze()


def test_class_definition(my_maze):
    """010A Class is called Maze"""
    assert type(my_maze) == Maze


def test_structure_type(my_maze):
    """020A Type of structure is a list"""
    assert type(my_maze.structure) == list


def test_maze_properties(my_maze):
    """030A Check all the properties"""
    assert type(my_maze.__class__.structure) == property
    assert type(my_maze.__class__.movements_player) == property
    assert type(my_maze.__class__.items) == property
    assert type(my_maze.__class__.locations) == property
    assert type(my_maze.__class__.player) == property


@patch('builtins.open', mock_open(read_data="   XXXX\n   XX  "))
def test_load_all_from_file(my_maze):
    """040A Test if the data is loading correctly by checking the length of the list formed"""
    my_maze._load_all_from_file()
    assert len(my_maze.structure) == 2


@patch('builtins.open', mock_open(read_data="   XXXX\n   XX  "))
def test_check_position(my_maze):
    """050A Returns True if coordinates entered is an empty space, false if a wall (‘X’) """
    my_maze._load_all_from_file()
    assert my_maze.check_position(0, 2)
    assert my_maze.check_position(0, 5) == False


def test_find_random_spot(my_maze):
    """060A Returns the row and col tuple if the random spot is an empty space. Uses check_position method """
    my_maze._load_all_from_file()
    row_value, col_value = my_maze.find_random_spot()
    assert my_maze.check_position(row_value, col_value)


@patch('builtins.open', mock_open(read_data="   XXXX\nT   XX  "))
def test_is_item(my_maze):
    """ 070A Returns True if the position is neither a wall (“X”) nor an empty space (“ ”) """
    my_maze._load_all_from_file()
    assert my_maze.is_item(1, 0)


def test_move_player(my_maze):
    """ 080A Moves the player in the structure list based on the user input.  """
    my_maze._load_all_from_file()
    my_maze.locations["P"] = [0, 1]
    my_maze.move_player(0, 1)
    assert (my_maze.locations["P"][0] + my_maze.movements_player[0],
            my_maze.locations["P"][1] + my_maze.movements_player[1]) == (0, 2)


def test_is_exit(my_maze):
    """ 090A Returns True if the player’s location is the same as “E”’s location.  """
    my_maze._load_all_from_file()
    my_maze.locations["E"] = [0, 1]
    my_maze.locations["P"] = [0, 2]
    my_maze.move_player(0, -1)
    assert my_maze.is_exit([my_maze.locations["P"][0] + my_maze.movements_player[0],
                            my_maze.locations["P"][1] + my_maze.movements_player[1]])


def test_get_item(my_maze):
    """100A Returns true if the player lands on the same position as an item and makes the value of the item in the locations dictionary to be None.  """
    my_maze._load_all_from_file()
    my_maze.locations["B"] = (0, 1)
    my_maze.locations["P"] = [0, 2]
    my_maze.move_player(0, -1)
    assert my_maze.get_item() and my_maze.locations["B"] == None


def test_generate_random_spots(my_maze):
    """110A Generates 7 random spots and puts items, player and exit in those spots.  """
    my_maze._load_all_from_file()
    my_maze.generate_random_spots()
    locations_list = list()
    for item in my_maze.items:
        locations_list.append(my_maze.locations[item])
    # if this is True, that means the items are being placed at different positions
    assert set(locations_list)
    # since there are 7 items to be placed in total
    assert len(locations_list) == 7
    print(locations_list)
