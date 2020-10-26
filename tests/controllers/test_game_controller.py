import pytest

from controllers.game_controller import GameController
from controllers.keyboard_controller import KeyboardController
from views.game_view import GameView
from models.maze import Maze

@pytest.fixture
def game():
    maze = Maze()
    maze._load_all_from_file("maze.txt")
    return GameController(maze)

def test_view(game):
    assert type(game._view) == GameView

def test_keyboard(game):
    assert type(game._keyboard_controller) == KeyboardController


# @patch("builtins.input", side_effect = "a")
def test_move_with_input(game):
    inputs = ["w", "s", "a", "d", "c"]
    shift = {
        "w": (-1, 0), 
        "s": (1, 0),
        "a": (0, -1),
        "d": (0, 1)
    }
    
    for i in inputs:
        current_location = game._maze.movements_player
        game.move_with_input(i)
        if i in shift:
            new_location = (shift[i][0] + current_location[0], shift[i][1] + current_location[1])
        else:
            new_location = current_location
        print("i : ",)
        print("current location : ", current_location)
        print("new location : ", new_location)
        assert new_location == game.player_current_location