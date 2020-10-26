import pytest

from unittest.mock import patch
from controllers.keyboard_controller import KeyboardController


@pytest.fixture
def keyboard():
    return KeyboardController()

def test_class_definition(keyboard):
    assert type(keyboard) == KeyboardController


def test_argument():
    with pytest.raises(TypeError):
        k = KeyboardController("w")

@patch("builtins.input", side_effect = "a")
def test_user_input(input_func, keyboard):
    assert keyboard.get_action() == "a"

# @patch("builtins.input", side_effect = "f")
# def test_input(keyboard):
#     with pytest.raises(IndexError):
#         patch.side_effect = "f"