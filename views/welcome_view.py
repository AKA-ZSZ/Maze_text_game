from .abstract_view import AbstractView


class WelcomeView(AbstractView):
    """ Display the Game Welcome view. Inherits from "AbstractView"
    """

    def _display_message(self):
        """Template method: display the initial welcome message

        Returns:
            str: welcome message
        """
        return "Welcome to our maze game!!"

    def _display_instructions(self):
        """Template method: display the game start instructions

        Returns:
            str: instruction message
        """
        return "Press any to start the game"
