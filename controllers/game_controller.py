from views.game_view import GameView
from .keyboard_controller import KeyboardController
from models.grid_size import GridSize

import pygame


class GameController:
    '''Call functions from GameView to display the maze. 
       Call functions from Maze to get position of player, items, and exit
       Set up how player will move based on "↑,↓,←,→" command'''

    def __init__(self, maze, window):
        """Constructor for GameController class

        Args:
            maze (Maze): instance of the Maze class
            window (pygame.Surface): display the pygame surface
        """
        self._maze = maze
        self._game_over = False
        self._view = GameView(maze, window)
        self._keyboard_controller = KeyboardController()

    @property
    def player_current_location(self):
        """Getter for player's current location

        Returns:
            (tuple): current location of the player
        """
        return (self._maze.locations["P"][0]+self._maze.movements_player[0], self._maze.locations["P"][1]+self._maze.movements_player[1])

    def run(self):
        """This is the main function that calls the methods that control the game based on user's input (↑,↓,←,→,q)
            The pygame window closes when user presses 'q'.
        """
        user_input = self._keyboard_controller.get_action()

        if user_input in ("up", "left", "down", "right"):
            self.move_with_input(user_input)

        elif user_input == "q":
            pygame.quit()

        self._view.display_maze()


    def move_with_input(self, user_input):
        """Gets user input from KeyboardController, matches it with the movement dict
            and updates the player position accordingly.

        Args:
            user_input (str): key pressed by the user
        """
        movement = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

        # position will not change if user_input is not a recognized command
        shift = movement.get(user_input, (0, 0))

        x = shift[0]
        y = shift[1]
        self._maze.move_player(x, y)

        # pygame - set new position in the window
        player_row = self.player_current_location[0]
        player_col = self.player_current_location[1]

        self._maze.player.rect.x = player_col*GridSize.SIZE
        self._maze.player.rect.y = player_row*GridSize.SIZE

        self._view.display_maze()
        if self._maze.get_item():
            self._view.get_items(self._maze.player.backpack)
