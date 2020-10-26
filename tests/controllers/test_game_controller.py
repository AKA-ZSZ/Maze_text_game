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


# def test_move_with_input(game):
#     inputs = ["w", "s", "a", "d"]
#     shift = {
#         "w": (-1, 0), 
#         "s": (1, 0),
#         "a": (0, -1),
#         "d": (0, 1)
#     }
#     # game._maze._locations["P"] = (3, 4)
#     # current_location = game._maze._locations["P"]
#     for i in inputs:
#         # current_location = (3, 4)
#         game._maze._locations["P"] = (3, 4)
#         current_location = game._maze._locations["P"]
#         game.move_with_input(i)
#         if i in shift:
#             new_location = (shift[i][0] + current_location[0], shift[i][1] + current_location[1])
#         else:
#             new_location = current_location
#         assert new_location == game.player_current_location

def test_move_up(game):
    game._maze._locations["P"] = (3, 4)
    current_location = game._maze._locations["P"]
    game.move_with_input("w")
    new_location = (current_location[0] - 1, current_location[1])
    assert new_location == game.player_current_location

def test_move_down(game):
    game._maze._locations["P"] = (3, 4)
    current_location = game._maze._locations["P"]
    game.move_with_input("s")
    new_location = (current_location[0] + 1, current_location[1])
    assert new_location == game.player_current_location

def test_move_left(game):
    game._maze._locations["P"] = (3, 4)
    current_location = game._maze._locations["P"]
    game.move_with_input("a")
    new_location = (current_location[0], current_location[1]-1)
    assert new_location == game.player_current_location

def test_move_right(game):
    game._maze._locations["P"] = (3, 4)
    current_location = game._maze._locations["P"]
    game.move_with_input("d")
    new_location = (current_location[0], current_location[1]+1)
    assert new_location == game.player_current_location