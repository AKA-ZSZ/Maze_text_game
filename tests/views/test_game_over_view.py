from views.game_over_view import GameOverView
import pytest

@pytest.fixture
def game_over_instance():
    maze = GameOverView(True)
    return maze


def test_class_definition(game_over_instance):
    """ 010A test: the class is called GameOverView"""
    assert type(game_over_instance) == GameOverView


def test_init_arguments():
    """ 020A test: the constructor takes one argument"""
    with pytest.raises(TypeError):
        maze = GameOverView()
    with pytest.raises(TypeError):
        maze1 = GameOverView("win","lose")


def test_init_maze():
    """ 020B test: maze must be Boolean"""
    with pytest.raises(ValueError):
        maze = GameOverView("winer")
    with pytest.raises(ValueError):
        maze = GameOverView(123)


def test_display_result_behavior(game_over_instance):
    """ 030A test behavior: if display result prints correct text on codition"""
    assert game_over_instance._display_message() == "You won the game, Congratulations"
