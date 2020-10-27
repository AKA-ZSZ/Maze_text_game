import pytest

from unittest.mock import patch
from controllers.keyboard_controller import KeyboardController


@pytest.fixture
def keyboard():
    return KeyboardController()

def test_class_definition(keyboard):
    '''010A the class is called KeyboardController'''
    assert type(keyboard) == KeyboardController

def test_argument():
    '''020A the constructor does not receive arguments'''
    with pytest.raises(TypeError):
        k = KeyboardController("w")

@patch("builtins.input", side_effect = "a")
def test_user_input(input_func, keyboard):
    '''030A returns user_input'''
    assert keyboard.get_action() == "a"
