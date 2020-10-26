import pytest

from controllers.game_over_controller import GameOverController
from models.maze import Maze

def test_class_definition():
    g = GameOverController(Maze())
    assert type(g) == GameOverController

def test_game_over_controller_argument():
    with pytest.raises(TypeError):
        g = GameOverController()

