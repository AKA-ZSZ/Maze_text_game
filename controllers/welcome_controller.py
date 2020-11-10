from views.welcome_view import WelcomeView
from .keyboard_controller import KeyboardController


class WelcomeController:
    '''Call functions from WelcomeView to display welcome messages'''

    def __init__(self,window):
        self._keyboard_controller=KeyboardController()
        self._view=WelcomeView(window)

    def run(self):
        # call functions from WelcomeView to display messages
        self._view.display_message()
        self._view.display_instructions()

        # get user input from KeyboardController
        # user_input=self._keyboard_controller.get_action()
    
    def get_input(self):
        # get user input from KeyboardController
        return self._keyboard_controller.get_action()
