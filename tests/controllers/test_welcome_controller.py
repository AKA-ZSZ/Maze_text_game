import pytest

from controllers.welcome_controller import WelcomeController
from controllers.keyboard_controller import KeyboardController
from views.welcome_view import WelcomeView
import sys
from unittest.mock import patch

@pytest.fixture
def welcome():
    return WelcomeController()

def test_class_definition(welcome):
    '''010A the class is called WelcomeController'''
    assert type(welcome) == WelcomeController

def test_view(welcome):
    '''020A _view is an object of WelcomeView'''
    assert type(welcome._view) == WelcomeView

def test_keyboard(welcome):
    '''020B _keyboard_controller is an object of KeyboardController'''
    assert type(welcome._keyboard_controller) == KeyboardController


def test_display_message(welcome, capfd):
    '''030A calls function form WelcomeView to display messages'''
    welcome.run()
    out, err = capfd.readouterr()

    assert out == "Welcome to our maze game!!\nPress w/a/s/d to start the game\n"
