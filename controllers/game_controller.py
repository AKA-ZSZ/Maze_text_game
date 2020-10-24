from views.game_view import GameView
from keyboard_controller import KeyboardController

class GameController:
    def __init__(self, maze):
        self._maze = Maze(maze)
        self._game_over = False
        
    def run(self):
        pass