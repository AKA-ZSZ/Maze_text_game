from views.welcome_view import WelcomeView


def test_class_definition():
    """ 010A test: the class is called WelcomeView"""
    maze = WelcomeView()
    assert type(maze) == WelcomeView


def test_display_message():
    """ 020A test: display message print correct message text """
    maze = WelcomeView()
    assert maze._display_message() == "Welcome to our maze game!!"


def test_display_intructions():
    """ 030A test: display instructions prints correct instruction text"""
    maze = WelcomeView()
    assert maze._display_instructions() == "Press w/a/s/d to start the game"
