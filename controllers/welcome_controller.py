from views.welcome_view import WelcomeView
from .keyboard_controller import KeyboardController


class WelcomeController:
    '''Call functions from WelcomeView to display welcome messages'''

    def __init__(self,window):
        """Constructor for WelcomeController class

        Args:
            window (pygame.Surface): displays the pygame window
        """
        self._keyboard_controller=KeyboardController()
        self._view=WelcomeView(window)

    def run(self):
        """This is the main function that calls function from WelcomeView to display messages"""
        # call functions from WelcomeView to display messages
        self._view.display_message()
        self._view.display_instructions()

        # get user input from KeyboardController
        # user_input=self.get_input()
    
    def get_input(self):
        """Method to get user input

        Returns:
            str: key pressed by the user
        """
        # get user input from KeyboardController
        return self._keyboard_controller.get_action()
