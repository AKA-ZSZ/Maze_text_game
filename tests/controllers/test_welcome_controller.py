import pytest

from controllers.welcome_controller import WelcomeController
from controllers.keyboard_controller import KeyboardController
from views.welcome_view import WelcomeView
import sys
# from unittest.mock import patch

@pytest.fixture
def welcome():
    return WelcomeController()

def test_class_definition(welcome):
    assert type(welcome) == WelcomeController

def test_view(welcome):
    assert type(welcome._view) == WelcomeView

def test_keyboard(welcome):
    assert type(welcome._keyboard_controller) == KeyboardController

def test_display_message(welcome, capfd):
    welcome.run()
    # with capfd.disabled():
        
    # out = sys.stdout
    # print(out)
    
    out, err = capfd.readouterr()

    assert out == "Welcome to our maze game!!\nPress any to start the game\n"


# def test_display_instruction(welcome, capfd):
#     welcome._view.display_instructions()
#     out, err = capfd.readouterr()
#     assert out == "Press any to start the game\n"


# @patch("builtins.input", side_effect = "a")
# def test_get_action(input_func, welcome):
#      assert welcome._keyboard_controller.get_action() == "a"