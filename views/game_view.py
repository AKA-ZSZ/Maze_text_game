import pygame
from models.grid_size import GridSize

class GameView:
    """ Displays the maze, move options and the player items
    """

    def __init__(self, maze, window):
        """ initialize private attribute maze

        Args:
            maze (object): instance of the Maze class

        Raises:
            TypeError: maze must be object
        """
        if not isinstance(maze, object):
            raise TypeError("Maze must be object")

        self._maze = maze
        self._window= window
        self._window.fill((0, 0, 0))

        pygame.font.init()
        self._arial = pygame.font.SysFont('arial', 18)

        # initialization
        self.display_maze()
        pygame.display.update()

    def display_move_options(self):
        """ Public: prints move options
        """
        print(self._display_move_options())

    def display_maze(self):
        """ Public: prints maze text
        """

        print(self._display_maze()) # print text version to terminal

    def get_items(self, items):
        """ Public: prints item in backpack
        """
        print(self._get_items(items))

    def _get_items(self, items):
        """ Display items in player backpack

            Returns
                str: items in backpack text 
        """

        return f"""Get an item!\nYou have: {items}.\n"""

    def _display_move_options(self):
        """ Displays move options for users

        Returns:
            str: move options text
        """
        return "type w,a,s,d to move the player: "

    def create_text_surface(self,text):
        openSans = pygame.font.SysFont('open sans', 24)
        text_surface = openSans.render(text, True, (160, 0, 0))

        return text_surface

    def _display_maze(self):
        """ Display the maze

        Returns:
            str: maze text
        """

        # text version
        text = ""
        for line in self._maze.structure:
            text += ("").join(line)
            text += "\n"


        # pygame version
        if pygame.sprite.spritecollide(self._maze.player, self._maze._maze_items, dokill=True):
            self._maze._score += 1

        # the time
        self._maze._time_left=float(f"{30 - (pygame.time.get_ticks()/1000):.2f}")

        # move these to view?
        self._window.blit(self.create_text_surface(
            f"Score: {self._maze._score}"), (self._maze.row * GridSize.SIZE - GridSize.SIZE * 2, self._maze.col * GridSize.SIZE))
        self._window.blit(self.create_text_surface(
            f"{self._maze._time_left}s"), (0, self._maze.col * GridSize.SIZE))

        # move these to view?
        self._window.blit(self._maze.player.image, self._maze.player.rect)
        self._window.blit(self._maze.maze_exit.image, self._maze.maze_exit.rect)
        self._maze._wall.draw(self._window)
        self._maze._maze_items.draw(self._window)
        

        return text
