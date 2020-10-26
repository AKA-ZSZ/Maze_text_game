import pytest

from controllers.welcome_controller import WelcomeController
from views.welcome_view import WelcomeView

@pytest.fixture
def welcome():
    return WelcomeController()

def test_class_definition(welcome):
    assert type(welcome) == WelcomeController

def test_view(welcome):
    assert type(welcome._view) == WelcomeView

