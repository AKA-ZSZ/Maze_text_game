from .abstract_view import AbstractView


class WelcomeView(AbstractView):

    def _display_message(self):
        return "Welcome to our maze game!!"

    def _display_instructions(self):
        return "Type s to start the game"
