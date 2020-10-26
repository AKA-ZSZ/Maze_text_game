from views.game_view import GameView
from .keyboard_controller import KeyboardController


class GameController:
    def __init__(self, maze):
        self._maze = maze
        self._game_over = False
        self._maze.generate_random_spots()
        self._view = GameView(maze)
        self._keyboard_controller = KeyboardController()


    @property
    def player_current_location(self):
        return (self._maze.locations["P"][0]+self._maze.movements_player[0], self._maze.locations["P"][1]+self._maze.movements_player[1])


    def run(self):

        # call display_maze() to display the maze
        self._view.display_maze()

        while not self._game_over:
            # giving player insturctions of commands
            self._view.display_move_options()

            user_input = self._keyboard_controller.get_action()

            self.move_with_input(user_input)

            # if 'P' reaches the exit, game over condition triggered
            if self._maze.is_exit(self.player_current_location):
            # if self._maze.is_exit(self.maze.movements.player):
                self._game_over=True
            
        return self._game_over


    def move_with_input(self, user_input):
        movement = {
            "w": (-1, 0),
            "s": (1, 0),
            "a": (0, -1),
            "d": (0, 1)
        }

        
        shift = movement.get(user_input, (0, 0))
        # if user_input in movement:
        x = shift[0]
        y = shift[1]
        self._maze.move_player(x, y)
        self._view.display_maze()
        if self._maze.get_item():
            self._view.get_items(self._maze.player.backpack)
    
        
