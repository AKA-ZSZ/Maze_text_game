from views.game_over_view import GameOverView
import pytest


def test_class_definition():
    maze = GameOverView("win")
    assert type(maze) == GameOverView


def test_init_arguments():
    with pytest.raises(TypeError):
        maze = GameOverView()
    with pytest.raises(TypeError):
        maze1 = GameOverView("win","lose")


def test_init_maze():
    with pytest.raises(ValueError):
        maze = GameOverView("winer")


def test_display_result_behavior():
    maze = GameOverView("win")
    assert maze._display_message() == "You won the game, Congratulations"
