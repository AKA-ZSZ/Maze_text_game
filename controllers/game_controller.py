from views.game_view import GameView
from .keyboard_controller import KeyboardController
from models.grid_size import GridSize

import pygame


class GameController:
    '''Call functions from GameView to display the maze. 
       Call functions from Maze to get position of player, items, and exit
       Set up how player will move based on "w,a,s,d" command'''

    def __init__(self, maze, window):
        self._maze = maze
        # self.player = player
        self._game_over = False
        self._view = GameView(maze,window)
        self._keyboard_controller = KeyboardController()
        
    @property
    def player_current_location(self):
        return (self._maze.locations["P"][0]+self._maze.movements_player[0], self._maze.locations["P"][1]+self._maze.movements_player[1])

    def run(self):
        
        user_input = self._keyboard_controller.get_action()
        
        # keys = pygame.key.get_pressed()
        # if keys[pygame.locals.K_RIGHT]:
        #     if player_col + 1 < self._maze.row and self._maze.check_position(player_rol, player_col + 1):
        #         self.move_with_input("d")
        #         self._maze.player.rect.x = min(
        #             self._maze.player.rect.x + GridSize.SIZE, self._maze.row * GridSize.SIZE - GridSize.SIZE)
        # elif keys[pygame.locals.K_LEFT]:
        #     self.move_with_input("a")
        #     if self._maze.check_position(player_rol, player_col - 1):
        #         self.player.rect.x = max(
        #             self.player.rect.x - GridSize.SIZE, 0)
        # elif keys[pygame.locals.K_UP]:
        #     if self._maze.check_position(player_rol - 1, player_col):
        #         self.move_with_input("w")
        #         self.player.rect.y = max(
        #             self.player.rect.y - GridSize.SIZE, 0)
        # elif keys[pygame.locals.K_DOWN]:
        #     if player_rol + 1 < self._maze.col and self._maze.check_position(player_rol + 1, player_col):
        #         self.move_with_input("s")
        #         self.player.rect.y = min(
        #             self.player.rect.y + GridSize.SIZE, self._maze.col * GridSize.SIZE - GridSize.SIZE)
        
        if user_input in ("w","a","s","d"):
            
            self.move_with_input(user_input)
                
        elif user_input=="q":
            pygame.quit()

        self._view.display_maze()

        # # call display_maze() to display the maze
        # self._view.display_maze()

        # while not self._game_over:
        #     # giving player insturctions of commands
        #     self._view.display_move_options()

        #     user_input = self._keyboard_controller.get_action()

        #     self.move_with_input(user_input)

        #     # if 'P' reaches the exit, game over condition triggered
        #     if self._maze.is_exit(self.player_current_location):
        #         # if self._maze.is_exit(self.maze.movements.player):
        #         self._game_over = True

        # return self._game_over

    def move_with_input(self, user_input):
        movement = {
            "w": (-1, 0),
            "s": (1, 0),
            "a": (0, -1),
            "d": (0, 1)
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
