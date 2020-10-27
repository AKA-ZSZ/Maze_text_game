import pytest

from controllers.game_over_controller import GameOverController
from views.game_over_view import GameOverView
from models.maze import Maze

def test_class_definition():
    '''010A the class is called GameOverController'''
    g = GameOverController(Maze())
    assert type(g) == GameOverController

def test_game_over_controller_argument():
    '''020A the constructor takes one argument'''
    with pytest.raises(TypeError):
        g = GameOverController()

def test_display_win_message(capfd):
    '''030A call functions from GameOverView to display win message'''
    maze=Maze()
    maze._player._backpack={"S","M","T","R","G"}
    game = GameOverController(maze)
    game.run()
    
    out, err = capfd.readouterr()

    assert out == "You won the game, Congratulations\n"


def test_display_lose_message(capfd):
    '''030B call functions from GameOverView to display lose message'''
    maze=Maze()
    maze._player._backpack={"S","M"}
    game = GameOverController(maze)
    game.run()
    
    out, err = capfd.readouterr()

    assert out == "you lost\n"