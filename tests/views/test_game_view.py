from views.game_view import GameView
import pytest


@pytest.fixture
def game_view_instance():
    maze = GameView([["P"," ","X","E","X"],[" "," "," "," ","X"]])
    return maze


def test_class_definition(game_view_instance):
    assert type(game_view_instance) == GameView


def test_init_argument():
    with pytest.raises(TypeError):
        maze = GameView()
    with pytest.raises(TypeError):
        maze = GameView([],"as")

def test_init_maze(game_view_instance):
    assert isinstance(game_view_instance._maze,list)


def test_display_move_options(game_view_instance):
    assert "w" in game_view_instance._display_move_options()
    assert "s" in game_view_instance._display_move_options()

def test_display_maze(game_view_instance):
    assert game_view_instance._display_maze() == 'P XEX\n    X\n'
