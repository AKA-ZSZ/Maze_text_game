from views.welcome_view import WelcomeView
from .keyboard_controller import KeyboardController


class WelcomeController:
    def __init__(self):
        self._keyboard_controller=KeyboardController()
        self._view=WelcomeView()
    
    def run(self):
        self._view.display_message()
        # while True:
        #     user_input=self._keyboard_controller.get_action()

        #     if len(user_input):
        #         return True
        user_input=self._keyboard_controller.get_action()