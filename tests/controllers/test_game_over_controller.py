import pytest

from controllers.game_over_controller import GameOverController
from views.game_over_view import GameOverView
from models.maze import Maze

def test_class_definition():
    g = GameOverController(Maze())
    assert type(g) == GameOverController

def test_game_over_controller_argument():
    with pytest.raises(TypeError):
        g = GameOverController()

def test_display_win_message(capfd):
    # maze = GameOverView(True)
    maze=Maze()
    maze._player._backpack={"S","M","T","R","G"}
    game = GameOverController(maze)
    game.run()
    
    out, err = capfd.readouterr()

    assert out == "You won the game, Congratulations\n"


def test_display_lose_message(capfd):
    maze=Maze()
    maze._player._backpack={"S","M"}
    game = GameOverController(maze)
    game.run()
    
    out, err = capfd.readouterr()

    assert out == "you lost\n"