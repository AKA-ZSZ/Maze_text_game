from views.game_view import GameView
from .keyboard_controller import KeyboardController


class GameController:
    def __init__(self, maze):
        self._maze = maze
        self._game_over = False
        self._maze.generate_random_spots()
        self._view = GameView(maze)
        self._keyboard_controller = KeyboardController()

    def run(self):
        self._view.display_maze()
        self._view.display_move_options()

        while not self._game_over:
            self._view.display_move_options()

            user_input = self._keyboard_controller.get_action()
            # print(user_input)
            if user_input == "w":
                self._maze.move_player(-1, 0)
                self._view.display_maze()
                if self._maze.get_item():
                    self._view.get_items(self._maze.player.backpack)


            if user_input == "s":
                self._maze.move_player(1, 0)
                self._view.display_maze()
                if self._maze.get_item():
                    self._view.get_items(self._maze.player.backpack)

            if user_input == "a":
                self._maze.move_player(0, -1)
                self._view.display_maze()
                if self._maze.get_item():
                    self._view.get_items(self._maze.player.backpack)

            if user_input == "d":
                self._maze.move_player(0, 1)
                self._view.display_maze()
                if self._maze.get_item():
                    self._view.get_items(self._maze.player.backpack)

            player_current_location = (
                self._maze.locations["P"][0]+self._maze.movements_player[0], self._maze.locations["P"][1]+self._maze.movements_player[1])
            
            if self._maze.is_exit(player_current_location):
                self._game_over=True
            
        return self._game_over

            
