from views.game_view import GameView
from .keyboard_controller import KeyboardController

class GameController:
    def __init__(self, maze):
        self._maze = maze
        self._game_over = False
        self._view=GameView(maze)
        self._keyboard_controller=KeyboardController()
        
    def run(self):
        self._view.display_maze()
        self._view.display_move_options()
        while True:
            user_input=self._keyboard_controller.get_action()
