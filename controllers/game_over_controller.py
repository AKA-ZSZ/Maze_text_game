from views.game_over_view import GameOverView
from .keyboard_controller import KeyboardController

class GameOverController:
    def __init__(self,maze):
        self._maze=maze
        # self._keyboard_controller=KeyboardController()

        self._maze_result=(len(self._maze.player.backpack)==5)
        self._view=GameOverView(self._maze_result)

    def run(self):
        self._view.display_message()
