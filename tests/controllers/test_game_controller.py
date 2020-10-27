import pytest

from controllers.game_controller import GameController
from controllers.keyboard_controller import KeyboardController
from views.game_view import GameView
from models.maze import Maze

# from unittest.mock import patch
from unittest import mock
import builtins

@pytest.fixture
def game():
    maze = Maze()
    maze._load_all_from_file("maze.txt")
    return GameController(maze)

def test_class_definition(game):
    '''010A the class is called GameController'''
    assert type(game) == GameController

def test_view(game):
    '''020A _view is an object of GameView'''
    assert type(game._view) == GameView

def test_keyboard(game):
    '''020B _keyboard_controller is an object of KeyboardController'''
    assert type(game._keyboard_controller) == KeyboardController

def test_move_up(game):
    '''030A player can move up with command w'''
    game._maze._locations["P"] = (3, 4)
    current_location = game._maze._locations["P"]
    game.move_with_input("w")
    new_location = (current_location[0] - 1, current_location[1])
    assert new_location == game.player_current_location

def test_move_down(game):
    '''030B player can move down with command s'''
    game._maze._locations["P"] = (3, 4)
    current_location = game._maze._locations["P"]
    game.move_with_input("s")
    new_location = (current_location[0] + 1, current_location[1])
    assert new_location == game.player_current_location

def test_move_left(game):
    '''030C player can move left with command a'''
    game._maze._locations["P"] = (3, 4)
    current_location = game._maze._locations["P"]
    game.move_with_input("a")
    new_location = (current_location[0], current_location[1]-1)
    assert new_location == game.player_current_location

def test_move_right(game):
    '''030D player can move right with command d'''
    game._maze._locations["P"] = (3, 4)
    current_location = game._maze._locations["P"]
    game.move_with_input("d")
    new_location = (current_location[0], current_location[1]+1)
    assert new_location == game.player_current_location


def test_exit():
    '''040A check player reaches the exit'''
    maze=Maze()
    maze._load_all_from_file()
    game_controller=GameController(maze)

    game_controller._maze._locations["P"]=(3,4)
    game_controller._maze._locations["E"]=(3,3)

    with mock.patch.object(builtins, 'input', lambda: 'a'):
        result=game_controller.run()

        assert result==True
    
