from views.game_view import GameView
from models.maze import Maze

import pytest
import pygame


@pytest.fixture
def game_view_instance():
    maze = Maze()
    maze._load_all_from_file()
    maze.generate_random_spots()
    window = pygame.display.set_mode(
        (1000, 1000))
    view = GameView(maze, window)
    return view


def test_class_definition(game_view_instance):
    """ 010A test for class definition"""
    assert type(game_view_instance) == GameView


def test_init_argument():
    """ 020A test if constructor recieves two argument """
    with pytest.raises(TypeError):
        maze = GameView()
    with pytest.raises(TypeError):
        maze = GameView([], "as", "as")


def test_init_maze(game_view_instance):
    """ 020B test for type of maze"""
    assert isinstance(game_view_instance._maze, object)


def test_display_maze(game_view_instance):
    """ 030A test if display maze prints correct maze"""
    assert "P" in game_view_instance._display_maze()
    assert "E" in game_view_instance._display_maze()


def test_display_move_options(game_view_instance):
    """ 040A test if display_move_options prints correct options """
    assert "w" in game_view_instance._display_move_options()
    assert "s" in game_view_instance._display_move_options()


def test_get_items(game_view_instance):
    """ 050A test for displaying player's backpack"""
    assert "You have:" in game_view_instance._get_items(
        ["M", "T", "R", "S", "G"])
    assert "M", "T" in game_view_instance._get_items(["M", "T", "R", "S", "G"])
