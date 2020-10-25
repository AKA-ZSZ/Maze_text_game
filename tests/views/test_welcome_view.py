from views.welcome_view import WelcomeView


def test_class_definition():
    maze = WelcomeView()
    assert type(maze) == WelcomeView


def test_display_message():
    maze = WelcomeView()
    assert maze._display_message() == "Welcome to our maze game!!"
